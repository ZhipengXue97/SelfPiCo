# Extracted from https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
def display_all(df):     # For any Dataframe df
   with pd.option_context('display.max_rows',1000): # Change number of rows accordingly
      with pd.option_context('display.max_columns',1000): # Change number of columns accordingly
          display(df)

