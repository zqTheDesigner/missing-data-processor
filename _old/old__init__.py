import pandas as pd
from ..processor import Processor

# The name datamender came from chatGPT 2022-Dec-09
class Mender:
    def __init__(self):
        """
        Initialize data mender, there will be 3 elements in data mender

        mender.original is the raw df read from the csv url.

        mender.focused comes from original, but remove all the unnecessary columns and rows.

        mender.sample is taking certain percentage from focused data,
        so can perform calculations fast.
        """
        # print("Data Mender initialized")
        self.original = Processor()
        self.focused = Processor()
        self.sample = Processor()

    def read_csv(self, file_path):
        """
        Read csv from file path as pandas DataFrame, then assign to original
        """
        if hasattr(self, "df"):
            raise RuntimeError("CSV already exist in Mender")

        self.df = pd.read_csv(file_path)

        # print("CSV file read successfully")
        self.original.df = self.df

    def set_focus(self, rows=None, columns=None):
        """
        Set focused rows and columns.
        Row number must be within original row index, row takes an array of index number
        Columns must be original csv's columns, it must be an array
        """
        if rows == None and columns == None:
            raise RuntimeError("Focused row or column or both must be provided")
        if columns is not None:
            self.focused.df = self.original.df[columns]
        if rows is not None:
            self.focused.df = self.focused.df.iloc[rows]
