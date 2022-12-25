from pandas.api.types import is_numeric_dtype


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


def impute(df, columns, strategies, inplace, capture_likelihood):
    """
    strategies: an array of functions from ImputationStrategies
    """
    if capture_likelihood:
        for column in columns:
            df[column+"__is-missing"] = df[columns].isnull().astype(int)

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
