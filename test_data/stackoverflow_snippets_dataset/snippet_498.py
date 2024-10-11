# Extracted from https://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-output-from-series-to-dataframe
import pandas as pd

grouped_df = df1.groupby( [ "Name", "City"] )

pd.DataFrame(grouped_df.size().reset_index(name = "Group_Count"))

