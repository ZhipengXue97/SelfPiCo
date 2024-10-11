# Extracted from https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
import string

def match(a,b):
    a,b = a.lower(), b.lower()
    error = 0
    for i in string.ascii_lowercase:
            error += abs(a.count(i) - b.count(i))
    total = len(a) + len(b)
    return (total-error)/total

if __name__ == "__main__":
    print(match("pple inc", "Apple Inc."))

