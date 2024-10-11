# Extracted from ./data/repos/flask/src/flask/testing.py
kwargs["environ_base"] = self._copy_environ(kwargs.get("environ_base", {}))
builder = EnvironBuilder(self.application, *args, **kwargs)

try:
    exit(builder.get_request())
finally:
    builder.close()
