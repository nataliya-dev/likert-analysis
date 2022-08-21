
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

    def remove_outliers(self, col_names: list, vals: list) -> None:
        for col in col_names:
            col_name = col.upper()
            self.df.columns = self.df.columns.str.upper()

            if col_name not in self.df:
                print("Column name {} not found in {}".format(
                    col_name, self.df.name))
                continue

            self.df[col_name].replace('', np.nan, inplace=True)
            self.df.dropna(subset=[col_name], inplace=True)

            ousted = self.df.index[(self.df[col_name].isin(vals))]
            self.df.drop(ousted, inplace=True)

            print("{} outliers removed based on {} in {}".format(
                len(ousted), col_name, self.df.name))
