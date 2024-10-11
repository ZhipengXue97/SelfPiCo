# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH#12857
lets = list("ACDEFGHIJKLMNOP")
slen = 50
nseqs = 1000
words = [[np.random.choice(lets) for x in range(slen)] for _ in range(nseqs)]
df = DataFrame(words).astype("U1")
assert (df.dtypes == object).all()

# smoke tests; at one point this raised with 61 but not 60
repr(df)
repr(df.iloc[:60, :])
repr(df.iloc[:61, :])
