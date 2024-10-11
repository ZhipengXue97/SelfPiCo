# Extracted from https://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3
class python3Execfile(object):
    def _get_file_encoding(self, filename):
        with open(filename, 'rb') as fp:
            try:
                return tokenize.detect_encoding(fp.readline)[0]
            except SyntaxError:
                return "utf-8"

    def my_execfile(filename):
        globals['__file__'] = filename
        with open(filename, 'r', encoding=self._get_file_encoding(filename)) as fp:
            contents = fp.read()
        if not contents.endswith("\n"):
            # http://bugs.python.org/issue10204
            contents += "\n"
        exec(contents, globals, globals)

