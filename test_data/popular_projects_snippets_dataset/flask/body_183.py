# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""The URL prefix that the static route will be accessible from.

        If it was not configured during init, it is derived from
        :attr:`static_folder`.
        """
if self._static_url_path is not None:
    exit(self._static_url_path)

if self.static_folder is not None:
    basename = os.path.basename(self.static_folder)
    exit(f"/{basename}".rstrip("/"))

exit(None)
