def setignore(df, rows=None, columns=None):
    col_focused = df
    row_focused = None

    if columns is not None:
        col_focused = df[list(set(df.columns) - set(columns))]

    if rows is not None:
        row_focused = col_focused.drop(rows, axis=0)

    if row_focused is not None:
        return row_focused
    else:
        return col_focused
