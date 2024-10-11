# Extracted from https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python
def read_file(data_file):
    # data_file = '\rr\ex.xlsx'
    sheets = {}
    try:
        print("Reading file: "+data_file)
        sheets['df_1'] = pd.read_excel(open(data_file,'rb'), 'SheetSum')
    except Exception as excpt:
        print("Exception occurred", exc_info=True)
    return sheets

read_file(file)
shutil.move( file, dirpath +'\\processed_files')

def read_file(data_file):
    # data_file = '\rr\ex.xlsx'
    sheets = {}
    sheets_file = None
    try:
        print("Reading file: "+data_file)
        sheets_file = open(data_file,'rb')
        sheets['df_1'] = pd.read_excel(sheets_file, 'SheetSum')
    except Exception as excpt:
        print("Exception occurred", exc_info=True)
    finally:
        if sheets_file:
            sheets_file.close()
    return sheets

read_file(file)
shutil.move( file, dirpath +'\\processed_files')

