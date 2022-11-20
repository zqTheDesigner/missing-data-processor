import pandas as pd


def overview(df):
    """
    Takes a data frame and calculate some overall information about the
    data frame.

    This functions is similar to pandas describe method, but provide more
    additional insights.
    """

    ov_idx = [
        "Total Columns",
        "Total Rows",
        "Incomplete Rows Count",
        "Incomplete Rows (%)",
        "Incomplete Columns Count",
        "Total Data Count",
        "Missing Data Count",
        "Missing Data (%)",
    ]
    ov = pd.DataFrame(index=ov_idx)

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    total_data = df.count().sum()
    incomplete_rows = df[df.isna().any(axis=1)].shape[0]
    incomplete_columns = df[df.isna().any(axis=1)].shape[1]
    missing_data = df.isna().sum().sum()

    ov.at["Total Columns", "Value"] = total_columns
    ov.at["Total Rows", "Value"] = total_rows
    ov.at["Incomplete Rows Count"] = incomplete_rows
    ov.at["Incomplete Rows (%)"] = round(incomplete_rows / total_rows, 4) * 100
    ov.at["Incomplete Columns Count"] = incomplete_columns
    ov.at["Total Data Count"] = total_data
    ov.at["Missing Data Count"] = missing_data
    ov.at["Missing Data (%)"] = round(missing_data / total_data, 4) * 100

    ov.transpose()
    return ov
