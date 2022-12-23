def setfocus(df, rows=None, columns=None):
    col_focused = df
    row_focused = None

    if columns is not None:
        col_focused = df[columns]

    if rows is not None:
        if type(rows) is tuple:
            start, end, *_ = rows
            step = 1 

            try: step = rows[2]
            except IndexError : pass

            row_focused = col_focused.iloc[start:end:step]
        else:
            row_focused = col_focused.iloc[rows]

    if row_focused is not None :
        return row_focused
    else :
        return col_focused 
