# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
df = DataFrame(
    np.random.rand(4, 5).astype(np.complex64),
    index=list("abcd"),
    columns=list("ABCDE"),
)

path = tmp_path / setup_path
df.to_hdf(path, "df", format="table")
reread = read_hdf(path, "df")
tm.assert_frame_equal(df, reread)

df = DataFrame(
    np.random.rand(4, 5).astype(np.complex128),
    index=list("abcd"),
    columns=list("ABCDE"),
)

path = tmp_path / setup_path
df.to_hdf(path, "df", format="table", mode="w")
reread = read_hdf(path, "df")
tm.assert_frame_equal(df, reread)
