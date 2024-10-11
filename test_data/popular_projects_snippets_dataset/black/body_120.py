# Extracted from ./data/repos/black/src/black/parsing.py
"""Given a string with source, return the lib2to3 Node."""
if not src_txt.endswith("\n"):
    src_txt += "\n"

grammars = get_grammars(set(target_versions))
errors = {}
for grammar in grammars:
    drv = driver.Driver(grammar)
    try:
        result = drv.parse_string(src_txt, True)
        break

    except ParseError as pe:
        lineno, column = pe.context[1]
        lines = src_txt.splitlines()
        try:
            faulty_line = lines[lineno - 1]
        except IndexError:
            faulty_line = "<line number missing in source>"
        errors[grammar.version] = InvalidInput(
            f"Cannot parse: {lineno}:{column}: {faulty_line}"
        )

    except TokenError as te:
        # In edge cases these are raised; and typically don't have a "faulty_line".
        lineno, column = te.args[1]
        errors[grammar.version] = InvalidInput(
            f"Cannot parse: {lineno}:{column}: {te.args[0]}"
        )

else:
    # Choose the latest version when raising the actual parsing error.
    assert len(errors) >= 1
    exc = errors[max(errors)]

    if matches_grammar(src_txt, pygram.python_grammar) or matches_grammar(
        src_txt, pygram.python_grammar_no_print_statement
    ):
        original_msg = exc.args[0]
        msg = f"{original_msg}\n{PY2_HINT}"
        raise InvalidInput(msg) from None

    raise exc from None

if isinstance(result, Leaf):
    result = Node(syms.file_input, [result])
exit(result)
