# Extracted from ./data/repos/flask/src/flask/cli.py
#: Optionally the import path for the Flask application.
self.app_import_path = app_import_path
#: Optionally a function that is passed the script info to create
#: the instance of the application.
self.create_app = create_app
#: A dictionary with arbitrary data that can be associated with
#: this script info.
self.data: dict[t.Any, t.Any] = {}
self.set_debug_flag = set_debug_flag
self._loaded_app: Flask | None = None
