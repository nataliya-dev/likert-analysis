from context import utils

reader = utils.Reader()
path = "../data"
file_name = "gui_log.csv"
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
path = "../output/stats"
file = "gui_puzz_ttest.csv"
saver.init_file(path, file)

analyzer = utils.Analyzer(saver)

grp1 = df.loc[df[category_name] == 0]
grp2 = df.loc[df[category_name] == 1]

analyzer.two_group_ttest(grp1, grp2)
