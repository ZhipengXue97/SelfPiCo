# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH 38125: do not stringify file objects that are also path-like
fsspec = pytest.importorskip("fsspec")
with tm.ensure_clean() as path:
    with fsspec.open(f"file://{path}", mode="wb") as fsspec_obj:
        assert fsspec_obj == icom.stringify_path(fsspec_obj)
