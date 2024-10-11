# Extracted from https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
"foo" in "foobar"
True
"foo" in "Foobar"
False
"foo" in "Foobar".lower()
True
"foo".capitalize() in "Foobar"
True
"foo" in ["bar", "foo", "foobar"]
True
"foo" in ["fo", "o", "foobar"]
False
["foo" in a for a in ["fo", "o", "foobar"]]
[False, False, True]

