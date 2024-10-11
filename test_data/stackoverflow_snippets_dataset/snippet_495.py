# Extracted from https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
a = "123abc"
t = re.match("[a-z]+",a)
t = re.search("[a-z]+",a)

