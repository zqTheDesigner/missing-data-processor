def amend_column(df, column, func, inplace, *args, **kwargs):
    amended = df[column].apply(func, **kwargs)

    print(kwargs)

    if inplace:
        df[column] = amended
    else:
        df[column + "__amended"] = amended
