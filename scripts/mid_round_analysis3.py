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
path = "../output/stats"
file = "grp_for_grp_ttest.csv"
saver.init_file(path, file)

analyzer = utils.Analyzer(saver)

grp1 = df.loc[df[category_name] == 0]
grp2 = df.loc[df[category_name] == 1]
sub_group_col = "Puzzle Number"

i_list = [1, 2, 3, 4]
j_list = [2, 3, 4, 1]


def analyze_all_puzz(grp1, grp2, grp_str):
    for idx, puzz_num in enumerate(i_list):
        puzzi = puzz_num
        puzzj = j_list[idx]
        print(" Group 1: Analyzing puzzle number: ", puzzi)
        grp1_puzzi = grp1.loc[grp1[sub_group_col] == puzzi]
        print(" Group 2: Analyzing puzzle number: ", puzzj)
        grp2_puzzi = grp2.loc[grp2[sub_group_col] == puzzj]
        qn_str = "puzz" + str(puzzi) + "," + "puzz" + str(puzzj)
        added_str = grp_str + "," + qn_str
        analyzer.two_group_ttest(grp1_puzzi, grp2_puzzi, added_str)


analyze_all_puzz(grp1, grp1, "grp1,grp1")
analyze_all_puzz(grp2, grp2, "grp2,grp2")
