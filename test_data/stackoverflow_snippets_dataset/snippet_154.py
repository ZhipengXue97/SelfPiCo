# Extracted from https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python
query = " ".join([
    'SELECT * FROM "TableName"',
    'WHERE "SomeColumn1"=VALUE',
    'ORDER BY "SomeColumn2"',
    'LIMIT 5;'
])

