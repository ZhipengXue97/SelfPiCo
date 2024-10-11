# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 51015 if conn = sqlite_iris_str
conn = request.getfixturevalue(conn)
iris_frame = read_sql_table("iris", conn)
check_iris_frame(iris_frame)
iris_frame = pd.read_sql("iris", conn)
check_iris_frame(iris_frame)
