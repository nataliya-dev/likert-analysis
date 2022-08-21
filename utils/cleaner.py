
import numpy as np
import pandas as pd
import copy


class Cleaner:
    df = pd.DataFrame()

    def __init__(self) -> None:
        pass

    def set_df(self, df: pd.DataFrame) -> None:
        self.df = df

    def get_df(self) -> pd.DataFrame:
        return copy.deepcopy(self.df)

    def remove_outliers(self, col_name: str, vals: list) -> None:
        if col_name not in self.df:
            print("Column name {} not found".format(
                col_name))
            return

        ousted = self.df.index[(self.df[col_name].isin(vals))]
        self.df.drop(ousted, inplace=True)

        print("{} outliers removed based on {}".format(
            len(ousted), col_name))
