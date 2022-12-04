import pandas as pd

from .overview import overview as _overview
from .insights import insights as _insights
from .impute import impute as _impute


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

    def set_focus_columns(self, focused_columns):
        if focused_columns == "*":
            self.df = self.orig_df
        else:
            self.df = self.orig_df[focused_columns]

    def set_ignore_columns(self, ignored_columns):
        # Here assumed there are no duplicated values in header
        focused_columns = list(set(self.orig_df.columns) - set(ignored_columns))
        self.set_focus_columns(focused_columns)

    def set_ignore_rows(self, row_index):
        """
        Ignore (drop) rows by index.
        """
        self.df.drop(row_index, axis=0, inplace=True)

    def set_sample(self, n=None, frac=None, type="random"):
        """
        Extract a sample from self.df for continue experimental
        """
        self.sample = self.df.sample(n=n, frac=frac).sort_index()

    def overview(self):
        """
        Return a table of overview of focused data.
        """
        return _overview(self.df)

    def sample_overview(self):
        return _overview(self.sample)

    def insights(self):
        """
        Return a data frame contains detailed insights about
        the focused data.
        """
        return _insights(self.df)

    def sample_insights(self):
        return _insights(self.sample)

    def extract_incompletes(self):
        """
        Return a dataFrame contains all rows with one or more
        incomplete data.
        """
        return self.df[self.df.isnull().any(axis=1)]

    # All imputation functions
    def impute_sample(self, columns, strategies):
        """
        For each column in sample dataFrame, apply the default
        or provided imputation method.

        Every strategy will be applied to every columns
        """
        self.sample = _impute(self.sample, columns, strategies)
        pass

    def impute_sample_columns(self, columns):
        """
        Apply imputation method to the particular sample column
        """
        pass

    def impute_column(self):
        """
        Apply one or multiple imputation stragety to a particulart column
        """
        pass

    def impute(self):
        """
        Impute the entire dataFrame with a default or
        provided imputation method
        """
        pass

    def save(self):
        """
        Save out the current data frame
        TODO
        """
        pass

    def sample_plot_line(self):
        """
        Return matplot pyplot line chart for all numeric columns
        """
        pass

    def sample_plot_kde(self):
        """
        Return the kde chart for all numeric columns
        """
        pass

    def save_sample(self):
        """
        Save out the sample data frame
        """
        pass