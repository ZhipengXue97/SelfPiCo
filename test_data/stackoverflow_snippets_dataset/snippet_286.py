# Extracted from https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
l = ["1", "", "3", ""]

while True:
  try:
    l.remove("")
  except ValueError:
    break

