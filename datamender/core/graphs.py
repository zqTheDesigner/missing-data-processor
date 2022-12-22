import matplotlib.pyplot as plt
import math


def calc_plots_shape(df):
    """
    Calculate the shape of plots based on the amount of numerical data
    TODO: Define a max column number, else the graphs may be very small
    """
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).shape[1]

    rows = int(math.floor(math.sqrt(numeric_cols)))
    cols = int(math.ceil(numeric_cols / rows))
    return rows, cols


def graphs(df, kind):

    rows, columns = calc_plots_shape(df)

    df.plot(subplots=True, layout=(rows, columns), kind=kind)

    plt.show()
