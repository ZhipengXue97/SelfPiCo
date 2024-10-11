# Extracted from ./data/repos/flask/src/flask/sessions.py
def on_update(self) -> None:
    self.modified = True
    self.accessed = True

super().__init__(initial, on_update)
