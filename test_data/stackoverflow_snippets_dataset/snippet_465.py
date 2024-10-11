# Extracted from https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
with codecs.open( csv_file,  mode='w', encoding='utf-8') as out_csv:
     csv_out_file = csv.DictWriter(out_csv)

