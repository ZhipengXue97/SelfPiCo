# Extracted from ./data/repos/flask/src/flask/helpers.py
gen = generator_or_function(*args, **kwargs)  # type: ignore
exit(stream_with_context(gen))
