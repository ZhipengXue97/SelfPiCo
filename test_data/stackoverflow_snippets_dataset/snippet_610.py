# Extracted from https://stackoverflow.com/questions/944592/best-practice-for-using-assert
assert meaningless_identifier <= MAGIC_NUMBER_XXX, 'meaningless_identifier is greater than MAGIC_NUMBER_XXX!!!'

assert meaningless_identifier > MAGIC_NUMBER_XXX, 'reactor temperature above critical threshold'

assert meaningless_identifier > MAGIC_NUMBER_XXX, f'reactor temperature({meaningless_identifier }) above critical threshold ({MAGIC_NUMBER_XXX})'

assert a == b, 'a is not equal to b'

