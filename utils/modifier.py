import pandas as pd
import copy


class Modifier:

    df = pd.DataFrame()

    def __init__(self) -> None:
        pass

    def set_df(self, df: pd.DataFrame) -> None:
        self.df = df

    def get_df(self) -> pd.DataFrame:
        return copy.deepcopy(self.df)

    def set_criteria(self, col_name: str, grp_ids: list) -> None:
        self.col_name = col_name
        self.grp_ids = grp_ids

    def categorise(self, row: pd.DataFrame) -> int:
        for idx, grp in enumerate(self.grp_ids):
            if row[self.col_name] in (grp):
                return idx

    def create_category(self, new_col_name: str) -> None:
        self.df[new_col_name] = self.df.apply(
            lambda row: self.categorise(row), axis=1)

    def select(self, col_name: str, vals: list) -> None:
        ousted = self.df.index[~self.df[col_name].isin(vals)]
        self.df.drop(ousted, inplace=True)
