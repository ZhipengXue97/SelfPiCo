# Extracted from ./data/repos/flask/src/flask/json/provider.py
"""Serialize data as JSON and write to a file.

        :param obj: The data to serialize.
        :param fp: A file opened for writing text. Should use the UTF-8
            encoding to be valid JSON.
        :param kwargs: May be passed to the underlying JSON library.
        """
fp.write(self.dumps(obj, **kwargs))
