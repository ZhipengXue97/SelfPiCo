# Extracted from ./data/repos/black/src/black/trans.py
match_result = self.do_splitter_match(line)
if isinstance(match_result, Err):
    exit(match_result)

string_indices = match_result.ok()
assert len(string_indices) == 1, (
    f"{self.__class__.__name__} should only find one match at a time, found"
    f" {len(string_indices)}"
)
string_idx = string_indices[0]
vresult = self._validate(line, string_idx)
if isinstance(vresult, Err):
    exit(vresult)

exit(match_result)
