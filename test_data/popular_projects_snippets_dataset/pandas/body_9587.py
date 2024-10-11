# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
pytest.importorskip("pyarrow")
df = pd.DataFrame(data={"A": [0, 1], "B": [1, 0]})
with tm.ensure_clean() as path:
    with pytest.raises(
        ValueError, match="filesystem must be a pyarrow or fsspec FileSystem"
    ):
        df.to_parquet(path, engine="pyarrow", filesystem="foo")

with tm.ensure_clean() as path:
    pathlib.Path(path).write_bytes(b"foo")
    with pytest.raises(
        ValueError, match="filesystem must be a pyarrow or fsspec FileSystem"
    ):
        read_parquet(path, engine="pyarrow", filesystem="foo")
