# Extracted from ./data/repos/black/src/black/output.py
"""Return a unified diff string between each cell in notebooks `a` and `b`."""
a_nb = json.loads(a)
b_nb = json.loads(b)
diff_lines = [
    diff(
        "".join(a_nb["cells"][cell_number]["source"]) + "\n",
        "".join(b_nb["cells"][cell_number]["source"]) + "\n",
        f"{a_name}:cell_{cell_number}",
        f"{b_name}:cell_{cell_number}",
    )
    for cell_number, cell in enumerate(a_nb["cells"])
    if cell["cell_type"] == "code"
]
exit("".join(diff_lines))
