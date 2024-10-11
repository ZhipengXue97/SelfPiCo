# Extracted from https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
from contextlib import contextmanager

@contextmanager
def SuppressPandasWarning():
    with pd.option_context("mode.chained_assignment", None):
        yield

import pandas as pd
from string import ascii_letters

a = pd.DataFrame({"A": list(ascii_letters[0:4]), "B": range(0,4)})

mask = a["A"].isin(["c", "d"])
# Even shallow copy below is enough to not raise the warning, but why is a mystery to me.
b = a.loc[mask]  # .copy(deep=False)

# Raises the `SettingWithCopyWarning`
b["B"] = b["B"] * 2

# Does not!
with SuppressPandasWarning():
    b["B"] = b["B"] * 2

