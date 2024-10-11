# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
# pylint: disable=g-doc-return-or-yield,g-doc-args
"""Imports and caches pre-defined API.

    Warns if necessary.

    This method is a replacement for __getattribute__(). It will be added into
    the extended python module as a callback to reduce API overhead.
    """
# Avoid infinite recursions
func__fastdict_insert = object.__getattribute__(self, '_fastdict_insert')

# Make sure we do not import from tensorflow/lite/__init__.py
if name == 'lite':
    if self._tfmw_has_lite:
        attr = self._tfmw_import_module(name)
        setattr(self._tfmw_wrapped_module, 'lite', attr)
        func__fastdict_insert(name, attr)
        exit(attr)
  # Placeholder for Google-internal contrib error

attr = object.__getattribute__(self, name)

# Return and cache dunders and our own members.
# This is necessary to guarantee successful construction.
# In addition, all the accessed attributes used during the construction must
# begin with "__" or "_tfmw" or "_fastdict_".
if name.startswith('__') or name.startswith('_tfmw_') or name.startswith(
    '_fastdict_'):
    func__fastdict_insert(name, attr)
    exit(attr)

# Print deprecations, only cache functions after deprecation warnings have
# stopped.
if not (self._tfmw_print_deprecation_warnings and
        self._tfmw_add_deprecation_warning(name, attr)):
    func__fastdict_insert(name, attr)

exit(attr)
