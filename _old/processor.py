import pandas as pd


class Processor:
    def __init__(self):
        """
        self.df will eventually been assigned as a pandas DataFrame
        all the other processing will be based on self.df

        initialize with pd.DataFrame so other functions can take df
        methods easily
        """
        # print("Processor initiated")
        self.df = pd.DataFrame()

    def head(self, *args, **kwargs):
        """
        Refer to pandas.DataFrame.head method
        """
        return self.df.head(*args, **kwargs)
