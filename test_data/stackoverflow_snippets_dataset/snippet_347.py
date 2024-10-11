# Extracted from https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list
def all_perms(elements):
    if len(elements) <= 1:
        yield elements  # Only permutation possible = no permutation
    else:
        # Iteration over the first element in the result permutation:
        for (index, first_elmt) in enumerate(elements):
            other_elmts = elements[:index]+elements[index+1:]
            for permutation in all_perms(other_elmts): 
                yield [first_elmt] + permutation

