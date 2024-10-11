# Extracted from https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-and-then-filling-it
import pandas as pd

col_names =  ['A', 'B', 'C']
my_df  = pd.DataFrame(columns = col_names)
my_df

my_df.loc[len(my_df)] = [2, 4, 5]

my_dic = {'A':2, 'B':4, 'C':5}
my_df.loc[len(my_df)] = my_dic 

col_names =  ['A', 'B', 'C']
my_df2  = pd.DataFrame(columns = col_names)
my_df = my_df.append(my_df2)

