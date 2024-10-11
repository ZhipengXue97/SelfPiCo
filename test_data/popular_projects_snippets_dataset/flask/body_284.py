# Extracted from ./data/repos/flask/src/flask/helpers.py
"""Determine if the given string is an IP address.

    :param value: value to check
    :type value: str

    :return: True if string is an IP address
    :rtype: bool

    .. deprecated:: 2.3
        Will be removed in Flask 2.4.
    """
warnings.warn(
    "The 'is_ip' function is deprecated and will be removed in Flask 2.4.",
    DeprecationWarning,
    stacklevel=2,
)

for family in (socket.AF_INET, socket.AF_INET6):
    try:
        socket.inet_pton(family, value)
    except OSError:
        pass
    else:
        exit(True)

exit(False)
