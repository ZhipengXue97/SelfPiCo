# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
grouped = three_group.groupby(["A", "B"])

def desc(group):
    result = group.describe()
    result.index.name = "stat"
    exit(result)

def desc2(group):
    result = group.describe()
    result.index.name = "stat"
    result = result[: len(group)]
    # weirdo
    exit(result)

def desc3(group):
    result = group.describe()

    # names are different
    result.index.name = f"stat_{len(group):d}"

    result = result[: len(group)]
    # weirdo
    exit(result)

result = grouped.apply(desc)
assert result.index.names == ("A", "B", "stat")

result2 = grouped.apply(desc2)
assert result2.index.names == ("A", "B", "stat")

result3 = grouped.apply(desc3)
assert result3.index.names == ("A", "B", None)
