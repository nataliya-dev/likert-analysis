from scipy import stats
import pandas as pd


class Analyzer:

    def __init__(self, saver) -> None:
        self.saver = saver
        pass

    def two_group_ttest(self, grp1: pd.DataFrame, grp2: pd.DataFrame, append: str = "") -> None:
        for qn in grp1.columns:
            group1_qn_ans = grp1[qn]
            group2_qn_ans = grp2[qn]

            pval = 1.0
            try:
                pval = self.ttest(group1_qn_ans, group2_qn_ans)
            except:
                pass

            is_significant = 0
            if(pval <= 0.05):
                is_significant = 1

            save_line = []
            save_line.append(qn)
            save_line.append(append)
            save_line.append(pval)
            save_line.append(is_significant)
            self.saver.save(save_line)

    def ttest(self, df_grp_1: pd.DataFrame, df_grp2: pd.DataFrame) -> float:
        stat = []
        pval = 0
        try:
            stat, pval = stats.ttest_ind(df_grp_1, df_grp2)
        except TypeError as e:
            print(e)
            return 0
        except KeyError as e:
            print(e)
            return 0
        return pval

    def mwu(self, df_grp_1: pd.DataFrame, df_grp2: pd.DataFrame) -> float:
        stat = []
        pval = 0
        try:
            stat, pval = stats.mannwhitneyu(df_grp_1, df_grp2)
        except TypeError as e:
            print(e)
            return 0
        except KeyError as e:
            print(e)
            return 0
        return pval

    def normality_test(self, df: pd.DataFrame) -> None:
        print("Shapiro")
        try:
            stat, p = stats.shapiro(df)
        except ValueError as e:
            print(e)
            return

        print('Statistics=%.3f, p=%.3f' % (stat, p))
        alpha = 0.05
        if p > alpha:
            print('Sample looks Gaussian (fail to reject H0)')
        else:
            print('Sample does not look Gaussian (reject H0)')

        print("Agostino K^2 Test")
        stat, p = stats.normaltest(df)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        alpha = 0.05
        if p > alpha:
            print('Sample looks Gaussian (fail to reject H0)')
        else:
            print('Sample does not look Gaussian (reject H0)')
