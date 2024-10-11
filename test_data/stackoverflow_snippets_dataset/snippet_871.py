# Extracted from https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
def __lt__(self, other):
  return self.comparable_value < other.comparable_value

minValue = min(yourList, key=(lambda k: yourList[k]))

