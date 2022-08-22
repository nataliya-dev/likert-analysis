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
saver.init_folder("../output/GUIHistograms")

plotter = utils.Plotter(saver)
plotter.histogram(reader.df, category_name)

saver = utils.Saver()
saver.init_folder("../output/GUIBoxPlots")

plotter = utils.Plotter(saver)
plotter.box_plot(reader.df, category_name)
