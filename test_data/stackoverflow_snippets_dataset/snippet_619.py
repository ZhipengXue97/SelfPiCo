# Extracted from https://stackoverflow.com/questions/893333/multiple-variables-in-a-with-statement
with A() as a, B() as b:
    suite

with A() as a:
    with B() as b:
        suite

with get_conn() as conn, conn.cursor() as cursor:
    cursor.execute(sql)

