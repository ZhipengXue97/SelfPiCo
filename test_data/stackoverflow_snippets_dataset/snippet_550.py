# Extracted from https://stackoverflow.com/questions/13295735/how-to-replace-nan-values-by-zeroes-in-a-column-of-a-pandas-dataframe
import pandas

df = pandas.read_csv('somefile.txt')

df = df.fillna(0)

