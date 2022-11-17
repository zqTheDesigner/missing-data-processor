import pandas as pd


def overview(df):
    ''' 
    Takes a data frame and calculate some overall information about the
    data frame. 

    This functions is similar to pandas describe method, but provide more
    additional insights. 
    '''
    ov_idx = [
        "Total Columns",
        "Total Rows",
        "Incomplete Rows Count",
        "Incomplete Rows (%)",
        "Incomplete Columns Count",
        "Total Data Points",
        "Incomplete Data Points Count",
        "Incomplete Data (%)",
    ]
    ov = pd.DataFrame(index=ov_idx)

    ov.at["Total Columns", 'Value'] = df.shape[1]
    ov.at["Total Rows", 'Value'] = df.shape[0]

    ov.transpose()
    return ov
