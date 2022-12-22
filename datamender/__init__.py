from .core.overview import overview as _overview
from .core.insights import insights as _insights
from .core.graphs import graphs as _graphs
from .core.setfocus import setfocus as _setfocus

class Mender:
    def __init__(self, df):
        self.df = df

    def overview(self):
        return _overview(self.df)

    def insights(self):
        return _insights(self.df)

    def graphs(self, kind = "line"):
        _graphs(self.df, kind)
        pass

    def set_focus(self, rows = None, columns = None):
        self.df = _setfocus(self.df, rows, columns)

    def set_ignore(self):
        pass

    def impute_column(self):
        pass

    def impute(self):
        pass

    def normalize_column(self):
        pass

    def normalize(self):
        pass

    def encode_column(self):
        pass

    def encode(self):
        pass

    def split(self):
        pass

    def amend_column(self):
        pass

    def apply_impute(self, impute_strategy_map=None):
        pass

    def use_strategy(self, mender_strategy):
        pass