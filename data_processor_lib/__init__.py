import pandas as pd

from .overview import overview as _overview
from .insights import insights as _insights

class Processor:
    def __init__(self):
        print("Profiler initialized")

    def read_csv(self, filepath):
        # The data frame to be focused
        self.df = pd.read_csv(filepath)
        # Back up of the original data frame
        self.orig_df = self.df

    def head(self, *args):
        return self.df.head(*args)

    def columns(self):
        return self.df.columns

    def set_focus(self, focused_columns):
        if focused_columns == "*":
            self.df = self.orig_df
        else:
            self.df = self.orig_df[focused_columns]

    def set_ignore(self, ignored_columns):
        # Here assumed there are no duplicated values in header
        focused_columns = list(set(self.orig_df.columns) - set(ignored_columns))
        self.set_focus(focused_columns)

    def overview(self):
        return _overview(self.df)

    def insights(self):
        return _insights(self.df)