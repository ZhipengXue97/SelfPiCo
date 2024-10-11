# Extracted from https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte
con = psycopg2.connect(host = sys.argv[1],
port = sys.argv[2],dbname = sys.argv[3],user = sys.argv[4], password = sys.argv[5])

cursor = con.cursor()
sqlfile = open(path, 'r')

