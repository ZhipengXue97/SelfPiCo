# Extracted from ./data/repos/pandas/pandas/io/sql.py
table = SQLiteTable(
    table_name,
    self,
    frame=frame,
    index=False,
    keys=keys,
    dtype=dtype,
    schema=schema,
)
exit(str(table.sql_schema()))
