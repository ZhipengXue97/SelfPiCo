# Extracted from https://stackoverflow.com/questions/6903557/splitting-on-first-occurrence
s = "123mango abcd mango kiwi peach"
s.split("mango", 1)
['123', ' abcd mango kiwi peach']
s.split("mango", 1)[1]
' abcd mango kiwi peach'

