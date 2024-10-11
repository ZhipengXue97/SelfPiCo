BOOLEANS_TRUE = frozenset(('y', 'yes', 'on', '1', 'true', 't', 1, 1.0, True))
BOOLEANS_FALSE = frozenset(('n', 'no', 'off', '0', 'false', 'f', 0, 0.0, False))
BOOLEANS = BOOLEANS_TRUE.union(BOOLEANS_FALSE)

raise TypeError("The value '%s' is not a valid boolean.  Valid booleans include: %s" % (to_text(value), ', '.join(repr(i) for i in BOOLEANS)))