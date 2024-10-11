# Extracted from ./data/repos/flask/src/flask/debughelpers.py
try:
    exit(super().__getitem__(key))
except KeyError as e:
    if key not in request.form:
        raise

    raise DebugFilesKeyError(request, key).with_traceback(
        e.__traceback__
    ) from None
