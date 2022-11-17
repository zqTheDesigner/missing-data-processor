import pandas as pd


def insights(df):
    """
    Return a dataframe table of data insights of each column
    """
    ins_idx = [
        "Valid Data Count",
        "Valid Data (%)",
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
        "Unique Values"
        "Unique Values Count",
    ]

    ins = pd.DataFrame(index=ins_idx)

    # na_df = df.isnull()

    # print(na_df.head())

    # for k, v in na_df.items():
    #     ins.at['Missing Data Count', k] = len(v)

    for k, v in df.items():
        ins.at['Missing Data Count', k] = v.isnull().sum()
        ins.at['Valid Data Count', k] = len(v) - int(v.isnull().sum()) 

    return ins