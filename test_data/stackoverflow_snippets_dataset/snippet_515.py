# Extracted from https://stackoverflow.com/questions/1546226/is-there-a-simple-way-to-remove-multiple-spaces-in-a-string
def unPretty(S):
   # Given a dictionary, JSON, list, float, int, or even a string...
   # return a string stripped of CR, LF replaced by space, with multiple spaces reduced to one.
   return ' '.join(str(S).replace('\n', ' ').replace('\r', '').split())

