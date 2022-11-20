import pandas as pd


def insights(df):
    """
    Return a dataframe table of data insights of each column
    """
    ins_idx = [
        "Valid Data Count",
        "Missing Data Count",
        "Missing Data (%)",
        "Data Type",
        "Mean",
        "Median",
        "Min",
        "Max",
        "Standard Deviation",
        "25%",
        "75%",
        "Mode Value",
        "Mode Count",
        "Unique Values" "Unique Values Count",
    ]

    ins = pd.DataFrame(index=ins_idx)

    # Fill up entire data frame with '-', because NaN is visually confusing
    for k, v in df.items():
        for n in ins_idx:
            ins.at[n, k] = "-"

    for k, v in df.items():
        missing_data = v.isnull().sum()
        total_data = v.count().sum()
        ins.at["Valid Data Count", k] = total_data
        ins.at["Missing Data Count", k] = missing_data
        ins.at["Missing Data (%)", k] = round(missing_data / total_data, 4) * 100
        ins.at["Data Type", k] = v.dtype

    for k, v in df.mean(skipna=True, numeric_only=True).items():
        mean = round(v, 2)
        ins.at["Mean", k] = mean

    for k, v in df.median(skipna=True, numeric_only=True).items():
        median = round(v, 2)
        ins.at["Median", k] = median

    for k, v in df.min(skipna=True, numeric_only=True).items():
        min = round(v, 2)
        ins.at["Min", k] = min

    for k, v in df.max(skipna=True, numeric_only=True).items():
        max = round(v, 2)
        ins.at["Max", k] = max

    return ins
