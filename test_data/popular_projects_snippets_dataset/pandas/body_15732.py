# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# ~ ####
expr = "~lhs"

# series
# float raises
lhs = Series(np.random.randn(5))
if engine == "numexpr":
    msg = "couldn't find matching opcode for 'invert_dd'"
    with pytest.raises(NotImplementedError, match=msg):
        result = pd.eval(expr, engine=engine, parser=parser)
else:
    msg = "ufunc 'invert' not supported for the input types"
    with pytest.raises(TypeError, match=msg):
        pd.eval(expr, engine=engine, parser=parser)

# int raises on numexpr
lhs = Series(np.random.randint(5, size=5))
if engine == "numexpr":
    msg = "couldn't find matching opcode for 'invert"
    with pytest.raises(NotImplementedError, match=msg):
        pd.eval(expr, engine=engine, parser=parser)
else:
    expect = ~lhs
    result = pd.eval(expr, engine=engine, parser=parser)
    tm.assert_series_equal(expect, result)

# bool
lhs = Series(np.random.rand(5) > 0.5)
expect = ~lhs
result = pd.eval(expr, engine=engine, parser=parser)
tm.assert_series_equal(expect, result)

# float
# int
# bool

# object
lhs = Series(["a", 1, 2.0])
if engine == "numexpr":
    with pytest.raises(ValueError, match="unknown type object"):
        pd.eval(expr, engine=engine, parser=parser)
else:
    msg = "bad operand type for unary ~: 'str'"
    with pytest.raises(TypeError, match=msg):
        pd.eval(expr, engine=engine, parser=parser)
