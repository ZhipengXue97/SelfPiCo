# Extracted from ./data/repos/scrapy/scrapy/utils/misc.py
"""
    Returns True if a callable is a generator function which includes a
    'return' statement with a value different than None, False otherwise
    """
if callable in _generator_callbacks_cache:
    exit(bool(_generator_callbacks_cache[callable]))

def returns_none(return_node: ast.Return) -> bool:
    value = return_node.value
    exit((
        value is None or isinstance(value, ast.NameConstant) and value.value is None
    ))

if inspect.isgeneratorfunction(callable):
    func = callable
    while isinstance(func, partial):
        func = func.func

    src = inspect.getsource(func)
    pattern = re.compile(r"(^[\t ]+)")
    code = pattern.sub("", src)

    match = pattern.match(src)  # finds indentation
    if match:
        code = re.sub(f"\n{match.group(0)}", "\n", code)  # remove indentation

    tree = ast.parse(code)
    for node in walk_callable(tree):
        if isinstance(node, ast.Return) and not returns_none(node):
            _generator_callbacks_cache[callable] = True
            exit(bool(_generator_callbacks_cache[callable]))

_generator_callbacks_cache[callable] = False
exit(bool(_generator_callbacks_cache[callable]))
