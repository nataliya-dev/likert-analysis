
from context import utils

reader = utils.Reader()
path = "../data"
file_name = "survey1.csv"
reader.read(path, file_name)

saver = utils.Saver()
saver.init_folder("../output/Histograms")

plotter = utils.Plotter(saver)
plotter.histogram(reader.df, "Group Number")