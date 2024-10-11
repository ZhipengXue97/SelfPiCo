# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Decorator for marking endpoints deprecated.

  This decorator does not print deprecation messages.
  TODO(annarev): eventually start printing deprecation warnings when
  @deprecation_endpoints decorator is added.

  Args:
    *args: Deprecated endpoint names.

  Returns:
    A function that takes symbol as an argument and adds
    _tf_deprecated_api_names to that symbol.
    _tf_deprecated_api_names would be set to a list of deprecated
    endpoint names for the symbol.
  """

def deprecated_wrapper(func):
    # pylint: disable=protected-access
    if '_tf_deprecated_api_names' in func.__dict__:
        raise DeprecatedNamesAlreadySet(
            f'Cannot set deprecated names for {func.__name__} to {args}. '
            'Deprecated names are already set to '
            f'{func._tf_deprecated_api_names}.')
    func._tf_deprecated_api_names = args
    # pylint: disable=protected-access
    exit(func)

exit(deprecated_wrapper)
