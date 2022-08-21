from asyncio.proactor_events import _ProactorBasePipeTransport
import unittest
from context import utils
import pandas as pd

from utils import modifier


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                                'points': [5, 7, 7, 9, 12, 9, 9, 4],
                                'rebounds': [11, 8, 10, 6, 6, 5, 9, 12],
                                'blocks': [4, 7, 7, 6, 5, 8, 9, 10]})

    def test_cleaner(self):
        cleaner = utils.Cleaner()
        filter_col = 'team'
        outlier_vals = ['A', 'C']
        cleaner.set_df(self.df)
        cleaner.remove_outliers(filter_col, outlier_vals)
        df_cleaned = cleaner.get_df()

        found1 = df_cleaned[df_cleaned['team'].str.contains('A')]
        found2 = df_cleaned[df_cleaned['team'].str.contains('C')]

        self.assertTrue(found1.empty)
        self.assertTrue(found2.empty)

    def test_modifier_cateogry(self):
        modifier = utils.Modifier()
        modifier.set_df(self.df)
        grp1_pts = [i for i in range(0, 10)]
        grp2_pts = [i for i in range(10, 20)]
        modifier.set_criteria("points", [grp1_pts, grp2_pts])
        category_name = "NEW GROUP"
        modifier.create_category(category_name)
        df = modifier.get_df()

        self.assertTrue(category_name in df)
        self.assertTrue(len(df[category_name] == len(self.df["team"])))

    def test_modifier_select(self):
        modifier = utils.Modifier()
        modifier.set_df(self.df)
        modifier.select("blocks", [4, 7])
        df = modifier.get_df()

        self.assertTrue(len(df["blocks"]) == 3)
        self.assertTrue(df["blocks"].iat[0] == 4)
        self.assertTrue(df["blocks"].iat[1] == 7)
        self.assertTrue(df["blocks"].iat[2] == 7)


if __name__ == '__main__':
    unittest.main()
