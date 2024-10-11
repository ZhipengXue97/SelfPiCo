# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# GH 42320
pre_render = styler._copy(deepcopy=True)
styler.to_latex(
    column_format="rllr",
    position="h",
    position_float="centering",
    hrules=True,
    label="my lab",
    caption="my cap",
)

assert pre_render.table_styles == styler.table_styles
assert pre_render.caption == styler.caption
