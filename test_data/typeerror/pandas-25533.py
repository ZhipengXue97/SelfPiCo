try:
    if takeable:
        self._values[label] = value
    else:
        self.index._engine.set_value(self._values, label, value)
except KeyError:

    # set using a non-recursive method
    self.loc[label] = value