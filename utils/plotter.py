import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from utils.saver import Saver


class Plotter:

    fig_size = [10, 5]
    y_label = ""

    def __init__(self, saver: Saver) -> None:
        self.saver = saver
        self.init_figure()

    def init_figure(self) -> None:
        self.fig, self.ax = plt.subplots(
            figsize=(self.fig_size[0], self.fig_size[1]))

    def clear_ax(self) -> None:
        self.ax.cla()

    def box_plot(self, df: pd.DataFrame, x_col: str, grp_col: str = "") -> None:
        num_cols = len(df.columns)
        self.init_figure()
        x_col = x_col.upper()
        grp_col = grp_col.upper()
        for qn_num in range(num_cols):
            qn_str = df.columns[qn_num]
            if grp_col == "":
                sns.boxplot(x=df[x_col],
                            y=df[qn_str])
            else:
                sns.boxplot(x=df[x_col],
                            y=df[qn_str],
                            hue=df[grp_col])
            self.ax.set_title(qn_str)
            self.ax.set_ylabel(self.y_label)
            self.saver.save_img(str(qn_num))
            self.clear_ax()

    def histogram(self, df: pd.DataFrame, grp_col: str) -> None:
        self.init_figure()
        num_cols = len(df.columns)
        grp_col = grp_col.upper()
        for qn_num in range(num_cols):
            qn = df.columns[qn_num]
            try:
                sns.histplot(data=df, x=qn, hue=grp_col,
                             multiple="dodge", shrink=.8)
            except:
                continue
            self.saver.save_img(str(qn_num))
            self.clear_ax()

    def subgroup_histogram(self, grp1: list, grp2: list, bins: list) -> None:
        num_cols = len(grp1[0].columns)
        num_subgroups = len(grp1)

        for col in range(num_cols):
            self.fig, self.axs = plt.subplots(3, 2, sharey=True, figsize=(
                self.fig_size[0], self.fig_size[1]))
            self.axs = self.axs.flatten()

            qn = grp1[0].columns[col]
            for sub_group in range(num_subgroups):
                grp1_ans = grp1[sub_group]
                grp2_ans = grp2[sub_group]

                grp1_qn_answ = grp1_ans[qn]
                grp2_qn_answ = grp2_ans[qn]

                self.axs[sub_group].hist([grp1_qn_answ, grp2_qn_answ], bins=bins, label=[
                    'group1', 'group2'])
                self.axs[sub_group].legend(loc='upper left')
                self.axs[sub_group].set_title(
                    "Puzzle " + str(sub_group+1))

            self.fig.suptitle(qn)
            self.saver.save_img(str(col))
            for ax in self.axs:
                ax.cla()
