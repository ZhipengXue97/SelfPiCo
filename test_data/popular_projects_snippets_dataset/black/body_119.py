# Extracted from ./data/repos/black/src/black/parsing.py
if not target_versions:
    # No target_version specified, so try all grammars.
    exit([
        # Python 3.7-3.9
        pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords,
        # Python 3.0-3.6
        pygram.python_grammar_no_print_statement_no_exec_statement,
        # Python 3.10+
        pygram.python_grammar_soft_keywords,
    ])

grammars = []
# If we have to parse both, try to parse async as a keyword first
if not supports_feature(
    target_versions, Feature.ASYNC_IDENTIFIERS
) and not supports_feature(target_versions, Feature.PATTERN_MATCHING):
    # Python 3.7-3.9
    grammars.append(
        pygram.python_grammar_no_print_statement_no_exec_statement_async_keywords
    )
if not supports_feature(target_versions, Feature.ASYNC_KEYWORDS):
    # Python 3.0-3.6
    grammars.append(pygram.python_grammar_no_print_statement_no_exec_statement)
if any(Feature.PATTERN_MATCHING in VERSION_TO_FEATURES[v] for v in target_versions):
    # Python 3.10+
    grammars.append(pygram.python_grammar_soft_keywords)

# At least one of the above branches must have been taken, because every Python
# version has exactly one of the two 'ASYNC_*' flags
exit(grammars)
