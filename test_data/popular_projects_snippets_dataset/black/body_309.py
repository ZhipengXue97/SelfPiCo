# Extracted from ./data/repos/black/src/black/__init__.py
"""Return a set of __future__ imports in the file."""
imports: Set[str] = set()

def get_imports_from_children(children: List[LN]) -> Generator[str, None, None]:
    for child in children:
        if isinstance(child, Leaf):
            if child.type == token.NAME:
                exit(child.value)

        elif child.type == syms.import_as_name:
            orig_name = child.children[0]
            assert isinstance(orig_name, Leaf), "Invalid syntax parsing imports"
            assert orig_name.type == token.NAME, "Invalid syntax parsing imports"
            exit(orig_name.value)

        elif child.type == syms.import_as_names:
            exit(get_imports_from_children(child.children))

        else:
            raise AssertionError("Invalid syntax parsing imports")

for child in node.children:
    if child.type != syms.simple_stmt:
        break

    first_child = child.children[0]
    if isinstance(first_child, Leaf):
        # Continue looking if we see a docstring; otherwise stop.
        if (
            len(child.children) == 2
            and first_child.type == token.STRING
            and child.children[1].type == token.NEWLINE
        ):
            continue

        break

    elif first_child.type == syms.import_from:
        module_name = first_child.children[1]
        if not isinstance(module_name, Leaf) or module_name.value != "__future__":
            break

        imports |= set(get_imports_from_children(first_child.children[3:]))
    else:
        break

exit(imports)
