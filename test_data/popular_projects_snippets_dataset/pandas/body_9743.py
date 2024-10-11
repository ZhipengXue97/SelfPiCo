# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 26761
data = DataFrame({"date": datetime(9999, 1, 1)}, index=[0])
assert data.to_sql("test_datetime_obb", self.conn, index=False) == 1
result = sql.read_sql_table("test_datetime_obb", self.conn)
expected = DataFrame([pd.NaT], columns=["date"])
tm.assert_frame_equal(result, expected)
