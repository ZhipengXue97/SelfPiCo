# Extracted from ./data/repos/flask/src/flask/debughelpers.py
form_matches = request.form.getlist(key)
buf = [
    f"You tried to access the file {key!r} in the request.files"
    " dictionary but it does not exist. The mimetype for the"
    f" request is {request.mimetype!r} instead of"
    " 'multipart/form-data' which means that no file contents"
    " were transmitted. To fix this error you should provide"
    ' enctype="multipart/form-data" in your form.'
]
if form_matches:
    names = ", ".join(repr(x) for x in form_matches)
    buf.append(
        "\n\nThe browser instead transmitted some file names. "
        f"This was submitted: {names}"
    )
self.msg = "".join(buf)
