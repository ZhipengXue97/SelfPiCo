# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
path = os.path.join(csv_dir_path, "utf16_ex.txt")
parser = all_parsers
result = parser.read_csv(path, encoding="utf-16", sep="\t")
assert len(result) == 50
