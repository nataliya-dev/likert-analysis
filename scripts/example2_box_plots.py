
from context import utils

reader = utils.Reader()
path = "../data"
file_name = "survey2.csv"
reader.read(path, file_name)

modifier = utils.Modifier()
criteria_name = "ID Number"
grp1_ids = [i for i in range(20, 40)]
grp2_ids = [i for i in range(50, 70)]
modifier.set_df(reader.df)
modifier.set_criteria(criteria_name, [grp1_ids, grp2_ids])
category_name = "Group Number"
modifier.create_category(category_name)
df = modifier.get_df()

saver = utils.Saver()
saver.init_folder("../output/BoxPlots")

plotter = utils.Plotter(saver)
plotter.box_plot(df, "Puzzle Id", category_name)
