# Extracted from https://stackoverflow.com/questions/34962104/how-can-i-use-the-apply-function-for-a-single-column
df['Date'] = df['Date'].fillna('')
df['Date'] = df['Date'].apply(lambda x : ((datetime.datetime.strptime(str(x), '%m/%d/%Y') - datetime.timedelta(days=30*365)).strftime('%Y%m%d')) if x != '' else x)

