from context import utils
import pandas as pd

reader = utils.Reader()
path = "../data"
file_name = "gui_log.csv"
reader.read(path, file_name)

grp1_ids = [22, 23, 26, 27, 30]
grp2_ids = [20, 21, 24, 25, 28, 29]

modifier = utils.Modifier()
modifier.set_df(reader.get_df())
modifier.select("ID Number", grp1_ids)
grp1 = modifier.get_df()

grp1_select = pd.DataFrame(columns=grp1.columns)
for id in grp1_ids:
    df = grp1.loc[grp1["ID Number"] == id]
    grp1_select = grp1_select.append(df.iloc[[1]], ignore_index=True)
print(grp1_select)

modifier = utils.Modifier()
modifier.set_df(reader.get_df())
modifier.select("ID Number", grp2_ids)
grp2 = modifier.get_df()

grp2_select = pd.DataFrame(columns=grp2.columns)
for id in grp2_ids:
    df = grp2.loc[grp2["ID Number"] == id]
    grp2_select = grp2_select.append(df.iloc[[1]], ignore_index=True)
print(grp2_select)

saver = utils.Saver()
path = "../output/stats"
file = "gui_timer_ttest.csv"
saver.init_file(path, file)

analyzer = utils.Analyzer(saver)
analyzer.two_group_ttest(grp1_select, grp2_select)
