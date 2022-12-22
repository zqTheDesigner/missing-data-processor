def setfocus(df, rows=None, columns=None):
    _df = df
    
    if columns is not None:
        _df = df[columns]

    if rows is not None:
        pass

    return _df
