import pandas as pd


def overview(df):
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
