from context import utils

reader = utils.Reader()
path = "../data"
file_name = "survey1.csv"
reader.read(path, file_name)

cleaner = utils.Cleaner()
filter_col = "ID Number"
outlier_vals = [0, 50, 51]
cleaner.set_df(reader.df)
cleaner.remove_outliers(filter_col, outlier_vals)
reader.set_df(cleaner.df)

saver = utils.Saver()
path = "../output/stats"
file = "survey1_ttest.csv"
saver.init_file(path, file)

analyzer = utils.Analyzer(saver)
df = reader.df
grp1 = df.loc[df["Group Number"] == 1]
grp2 = df.loc[df["Group Number"] == 2]
analyzer.two_group_ttest(grp1, grp2)
print("Results written to {}".format(file))
