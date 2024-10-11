# Extracted from ./data/repos/black/src/black/linegen.py
# "import from" nodes store parentheses directly as part of
# the statement
if is_lpar_token(child):
    assert is_rpar_token(parent.children[-1])
    # make parentheses invisible
    child.value = ""
    parent.children[-1].value = ""
elif child.type != token.STAR:
    # insert invisible parentheses
    parent.insert_child(index, Leaf(token.LPAR, ""))
    parent.append_child(Leaf(token.RPAR, ""))
