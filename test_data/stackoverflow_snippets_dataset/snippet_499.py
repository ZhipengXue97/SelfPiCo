# Extracted from https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
import os
import imp

def importFromURI(uri, absl):
    mod = None
    if not absl:
        uri = os.path.normpath(os.path.join(os.path.dirname(__file__), uri))
    path, fname = os.path.split(uri)
    mname, ext = os.path.splitext(fname)

    if os.path.exists(os.path.join(path,mname)+'.pyc'):
        try:
            return imp.load_compiled(mname, uri)
        except:
            pass
    if os.path.exists(os.path.join(path,mname)+'.py'):
        try:
            return imp.load_source(mname, uri)
        except:
            pass

    return mod

