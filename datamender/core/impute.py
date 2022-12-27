import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, KNNImputer

# For phase 1, want to quickly get this feature done, so using
# these 2 global variable store a temporary sklearn imputed DataFrame
# These should be removed when refactor the Mender.impute() method
iterative_imputed = None
knn_imputed = None


class ImputationStrategies:
    """
    Each strategy always return a name prefix with the imputed column value
    """

    def mean(df, column):
        d_type = df.dtypes[column]
        if is_numeric_dtype(d_type):
            mean = df[column].mean(skipna=True)
            return "__mean", df[column].fillna(mean).astype(d_type)
        else:
            pass

    def median(df, column):
        d_type = df.dtypes[column]
        if is_numeric_dtype(d_type):
            median = df[column].median(skipna=True)
            return "__median", df[column].fillna(median).astype(d_type)
        else:
            pass

    def mode(df, column):
        d_type = df.dtypes[column]
        mode = df[column].mode()
        # Here need to use mode[0] to get the value
        return "__mode", df[column].fillna(mode[0]).astype(d_type)

    def sklearn_iterative(df, column):

        global iterative_imputed

        # Why need to check these?
        # Because the imputed function currently is passing column by column
        # But iterative_impute is processing the entire dataframe
        # We only need to run this once each time user called Mender.impute()
        if iterative_imputed is None:
            imputer = IterativeImputer(random_state=42)
            num_df = df.select_dtypes(include=["float64", "int64"])
            iterative_imputed = pd.DataFrame(imputer.fit_transform(num_df),
                                             columns=num_df.columns)
        return "__sklearn_iterative", iterative_imputed[column]

    def sklearn_knn(df, column):
        global knn_imputed

        if knn_imputed is None:
            imputer = KNNImputer(n_neighbors=2)
            num_df = df.select_dtypes(include=["float64", "int64"])
            knn_imputed = pd.DataFrame(imputer.fit_transform(num_df),
                                       columns=num_df.columns)
            return "__sklearn_knn", knn_imputed[column]


def impute(df, columns, strategies, inplace, capture_likelihood):
    """
    strategies: an array of functions from ImputationStrategies
    """

    if capture_likelihood:
        for column in columns:
            df[column + "__was-missing"] = df[columns].isnull().astype(int)

    if inplace:
        if len(strategies) > 1:
            raise TypeError(
                "To impute implace, please only provide single strategy is accepted"
            )

        for column in columns:
            for strategy in strategies:
                try:
                    _, value = strategy(df, column)
                    df[column] = value
                except Exception as e:
                    pass

    # This looks a bit wrong, probably refactor in future
    if not inplace:
        for column in columns:
            for strategy in strategies:
                try:
                    prefix, value = strategy(df, column)
                    df[column + prefix] = value
                except Exception as e:
                    pass

    # Reset the 2 global imputed temp dataframes
    # This should be refactored when refactor the impute mechanism
    global iterative_imputed
    global knn_imputed
    iterative_imputed = None
    knn_imputed = None
