# Extracted from https://stackoverflow.com/questions/1663807/how-do-i-iterate-through-two-lists-in-parallel
def custom_zip(seq1, seq2):
    it1 = iter(seq1)
    it2 = iter(seq2)
    while True:
        yield next(it1), next(it2)

