from context import utils
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pylab as pylab

reader = utils.Reader()
path = "../data"
file_name = "post_exp_survey.csv"
reader.read(path, file_name)

cleaner = utils.Cleaner()
filter_col = "ID Number"
outlier_vals = [0, 51]
cleaner.set_df(reader.df)
cleaner.remove_outliers(filter_col, outlier_vals)
reader.set_df(cleaner.df)

modifier = utils.Modifier()
criteria_name = "ID Number"
grp1_ids = [i for i in range(20, 40)]
grp2_ids = [i for i in range(49, 70)]
modifier.set_df(reader.df)
modifier.set_criteria(criteria_name, [grp1_ids, grp2_ids])
category_name = "GROUP NUMBER"
modifier.create_category(category_name)
df = modifier.get_df()

# saver = utils.Saver()
# saver.init_folder("../output/PostExpHistograms")

# plotter = utils.Plotter(saver)
# plotter.histogram(reader.df, category_name)

# saver = utils.Saver()
# saver.init_folder("../output/PostExpBoxPlots")

# plotter = utils.Plotter(saver)
# plotter.box_plot(reader.df, category_name)

saver = utils.Saver()
path = "../output/stats"
file = "post_exp_ttest.csv"
saver.init_file(path, file)

analyzer = utils.Analyzer(saver)
grp1 = df.loc[df[category_name] == 0]
grp2 = df.loc[df[category_name] == 1]

print("Num data points in group 1: ", len(grp1))
print("Num data points in group 2: ", len(grp2))

qn1 = "To what extent did you feel that it was your responsibility to perform well on the task?"
qn2 = "To what extent did you feel ownership for the task?"
qn3 = "To what extent did you feel obligated to perform well on the task?"

print(grp1[qn1])
np_11 = grp1[qn1].to_numpy()
np_12 = grp1[qn2].to_numpy()
np_13 = grp1[qn3].to_numpy()

np_21 = grp2[qn1].to_numpy()
np_22 = grp2[qn2].to_numpy()
np_23 = grp2[qn3].to_numpy()

qn1 = "...that it was your\nresponsibility to perform \nwell on the task?"
qn2 = "...ownership for\nthe task?"
qn3 = "...obligated to perform\nwell on the task?"

sns.set(font_scale=3)
sns.set(rc={'figure.figsize': (6, 3)})
sns.set_style('white')

data = [[qn1, np.mean(np_11), 'No Blame'], [qn1, np.mean(np_21), 'Blame'],
        [qn2, np.mean(np_12), 'No Blame'], [qn2, np.mean(np_22), 'Blame'],
        [qn3, np.mean(np_13), 'No Blame'],  [qn3, np.mean(np_23), 'Blame']]
df = pd.DataFrame(data, columns=[
                  'Survey Question', 'Likert Scale Response Avg.\n(1=Not at all, 7=Extremely)', 'Group'])

ax = sns.barplot(df, x='Survey Question',
                 y='Likert Scale Response Avg.\n(1=Not at all, 7=Extremely)', hue='Group')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
# plt.tight_layout()
ax.set(xlabel=None)
plt.title("To what extent did you feel...")


hatches = [" ", "\\\\"]
# Loop over the bars
for bars, hatch in zip(ax.containers, hatches):
    # Set a different hatch for each group of bars
    for bar in bars:
        bar.set_hatch(hatch)
ax.legend(title='Group', loc='lower right')
plt.tight_layout()
plt.ylim(1, 7)

plt.text(0, 6.1, "p=0.04", ha='center', va='bottom', color='k')
plt.text(1, 5.2, "p=0.046", ha='center', va='bottom', color='k')
plt.text(2, 6.0, "p=0.017", ha='center', va='bottom', color='k')

plt.show()
# analyzer.two_group_ttest(grp1, grp2)
