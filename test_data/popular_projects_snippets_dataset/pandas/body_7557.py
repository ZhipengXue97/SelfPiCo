# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
msg = f"`clines` value of {clines} is invalid."
with pytest.raises(ValueError, match=msg):
    styler.to_latex(clines=clines)
