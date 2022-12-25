def amend_column(df, column, func, inplace):
    amended = df[column].apply(func)

    if inplace:
        df[column] = amended
    else:
        df[column + "__amended"] = amended
