class ImputationStrategies:
    def mean_imputation(df, column):
        mean = df[column].mean(skipna=True)
        df[column + "_mean"] = df[column].fillna(mean).astype(float)

    def median_imputation(df, column):
        median = df[column].median(skipna=True)
        df[column + "_median"] = df[column].fillna(median).astype(float)


def impute(df, columns, strategies):
    """
    strategies: an array of functions from ImputationStrategies

    TODO: Column and strategy should take either single item of an array
    """
    for strategy in strategies:
        for column in columns:
            strategy(df, column)
    return df
