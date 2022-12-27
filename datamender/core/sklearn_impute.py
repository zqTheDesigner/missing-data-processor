import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, KNNImputer


def sklearn_impute(df, columns, strategy, inplace, remark='', *_, **kwargs):
    '''
    strategy: "iterative" or "knn"
    '''
    imputer = None

    # To check, what other numerical d types from pandas need to be selected here
    num_df = df.select_dtypes(include=["float64", "int64"])

    if strategy == "iterative":
        imputer = IterativeImputer(**kwargs)

    if strategy == "knn":
        imputer = KNNImputer(**kwargs)

    imputed = pd.DataFrame(imputer.fit_transform(num_df),
                           columns=num_df.columns)
    if inplace:
        for column in columns:
            df[column] = imputed[column]
    else:
        for column in columns:
            df[column + "__" + strategy + str(
                ("_" + remark if remark else ""))] = imputed[column]
