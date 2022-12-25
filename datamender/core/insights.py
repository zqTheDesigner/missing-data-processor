import pandas as pd


def get_value(v, k, to_round=2):
    if not k in v:
        return "-"

    if isinstance(v[k], float):
        return round(v[k], to_round)
    else:
        return v[k]


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
        "25% Quantile",
        "75% Quantile",
        "Mode",
        "Mode Count",
        "Mode (%)",
        "Unique Values Count",
        "Unique Values (%)",
    ]

    ins = pd.DataFrame(index=ins_idx)
    total_data = df.shape[0]

    # Fill up entire data frame with '-', because NaN is visually confusing
    # for k, v in df.items():
    #     for n in ins_idx:
    #         ins.at[n, k] = "-"

    for k, v in df.items():
        missing_data = v.isnull().sum()
        ins.at["Valid Data Count", k] = total_data
        ins.at["Missing Data Count", k] = missing_data
        ins.at["Missing Data (%)", k] = round(missing_data / total_data, 4) * 100
        ins.at["Data Type", k] = v.dtype

    mean = df.mean(skipna=True, numeric_only=True)
    median = df.median(skipna=True, numeric_only=True)
    min = df.min(skipna=True, numeric_only=True)
    max = df.max(skipna=True, numeric_only=True)
    std = df.std(skipna=True, numeric_only=True)
    quantile_25 = df.quantile(q=0.25, numeric_only=True)
    quantile_75 = df.quantile(q=0.75, numeric_only=True)
    mode = df.mode()

    for k in df.columns:
        ins.at["Mean", k] = get_value(mean, k)
        ins.at["Median", k] = get_value(median, k)
        ins.at["Min", k] = get_value(min, k)
        ins.at["Max", k] = get_value(max, k)
        ins.at["Standard Deviation", k] = get_value(std, k)
        ins.at["25% Quantile", k] = get_value(quantile_25, k)
        ins.at["75% Quantile", k] = get_value(quantile_75, k)
        ins.at["Mode", k] = mode[k][0]
        ins.at["Mode Count", k] = df[k].value_counts()[mode[k][0]]
        ins.at["Mode (%)", k] = round(df[k].value_counts()[mode[k][0]] / total_data, 4) * 100
        ins.at["Unique Values Count", k] = df[k].drop_duplicates().count()
        ins.at["Unique Values (%)", k] = (
            round(df[k].drop_duplicates().count() / df[k].count().sum(), 4) * 100
        )
        

    return ins
