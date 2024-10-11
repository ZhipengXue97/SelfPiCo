# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
if self.params:
    exit(f"%%{self.name} {self.params}")
exit(f"%%{self.name}")
