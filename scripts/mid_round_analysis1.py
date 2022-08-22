from context import utils


reader = utils.Reader()
path = "../data"
file_name = "rounds_survey.csv"
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

saver = utils.Saver()
saver.init_folder("../output/MidRoundHistogram")

grp1 = df.loc[df[category_name] == 0]
grp2 = df.loc[df[category_name] == 1]
sub_group_col = "Puzzle Number"

grp1_puzz = []
for i in range(1, 7):
    ans = grp1.loc[grp1[sub_group_col] == i]
    grp1_puzz.append(ans)

grp2_puzz = []
for i in range(1, 7):
    ans = grp2.loc[grp2[sub_group_col] == i]
    grp2_puzz.append(ans)

plotter = utils.Plotter(saver)
bins = [i for i in range(1, 8)]
plotter.fig_size = [10, 10]
plotter.subgroup_histogram(grp1_puzz, grp2_puzz, bins)

saver = utils.Saver()
saver.init_folder("../output/MidRoundBoxPlots")

plotter = utils.Plotter(saver)
plotter.box_plot(reader.df, sub_group_col, category_name)
