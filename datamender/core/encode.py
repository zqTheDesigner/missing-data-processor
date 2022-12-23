import pandas as pd


class EncodingStrategies:
    def one_hot(df, column, *_, **__):
        encoded = pd.get_dummies(df[column], prefix=column + "__")
        for (col_name, col_data) in encoded.items():
            df[col_name] = col_data

    def label_encoding(df, column, category_order_map):
        def encode(category):
            if pd.isnull(category) and "NaN" in category_order_map:
                return category_order_map["NaN"]
            elif pd.isnull(category) and "NaN" not in category_order_map:
                # If "NaN" is not provided, return real NaN value
                return pd.to_numeric("")
            else:
                return category_order_map[category]

        df[column + "__category"] = df[column].apply(encode)


def encode(df, column, strategy, inplace, category_order_map):
    strategy(df, column, category_order_map)

    if inplace:
        df.drop(columns=column, inplace=True, axis=1)
