# Extracted from https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
from terminaltables import AsciiTable

l = [
  ['Head', 'Head'],
  ['R1 C1', 'R1 C2'],
  ['R2 C1', 'R2 C2'],
  ['R3 C1', 'R3 C2']
]

table = AsciiTable(l)
print(table.table)

