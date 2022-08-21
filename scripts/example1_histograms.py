
from context import utils

reader = utils.Reader()
path = "../data"
file_name = "survey1.csv"
reader.read(path, file_name)

saver = utils.Saver()
folder_name = "../output/Histograms"
saver.init_folder(folder_name)

plotter = utils.Plotter(saver)
plotter.histogram(reader.df, "Group Number")
print("Histograms saved in {}".format(folder_name))
