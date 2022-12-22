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
        "Valid Data Count",
        "Missing Data Count",
        "Missing Data (%)",
    ]

    ov_columns = ["Value"]
    ov = pd.DataFrame(index=ov_idx, columns=ov_columns)

    total_rows, total_columns = df.shape
    valid_data = df.count().sum()
    incomplete = df[df.isna().any(axis=1)].shape
    incomplete_rows, incomplete_columns = incomplete
    missing_data = df.isna().sum().sum()

    ov.at["Total Columns", "Value"] = total_columns
    ov.at["Total Rows", "Value"] = total_rows
    ov.at["Incomplete Rows Count", "Value"] = incomplete_rows
    ov.at["Incomplete Rows (%)", "Value"] = round(incomplete_rows / total_rows, 4) * 100
    ov.at["Incomplete Columns Count", "Value"] = incomplete_columns
    ov.at["Total Data Count", "Value"] = total_columns * total_rows
    ov.at["Valid Data Count", "Value"] = valid_data
    ov.at["Missing Data Count", "Value"] = missing_data
    ov.at["Missing Data (%)", "Value"] = (
        round(missing_data / (total_columns * total_rows), 4) * 100
    )

    ov.transpose()
    return ov
