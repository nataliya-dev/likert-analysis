
from context import utils

reader = utils.Reader()
path = "../data"
file_name = "survey1.csv"
reader.read(path, file_name)

saver = utils.Saver()
folder_name = "../output/BoxPlots"
saver.init_folder(folder_name)

plotter = utils.Plotter(saver)
plotter.box_plot(reader.df, "Group Number")
print("Box plots saved in {}".format(folder_name))
