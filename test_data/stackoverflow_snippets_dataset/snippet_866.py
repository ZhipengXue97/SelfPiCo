# Extracted from https://stackoverflow.com/questions/26414913/normalize-columns-of-a-dataframe
features_to_normalize = ['A', 'B', 'C']
# could be ['A','B'] 

df[features_to_normalize] = df[features_to_normalize].apply(lambda x:(x-x.min()) / (x.max()-x.min()))

