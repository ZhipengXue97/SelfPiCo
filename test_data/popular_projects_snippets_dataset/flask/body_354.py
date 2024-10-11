# Extracted from ./data/repos/flask/src/flask/cli.py
"""Show all registered routes with endpoints and methods."""
rules = list(current_app.url_map.iter_rules())

if not rules:
    click.echo("No routes were registered.")
    exit()

ignored_methods = set() if all_methods else {"HEAD", "OPTIONS"}
host_matching = current_app.url_map.host_matching
has_domain = any(rule.host if host_matching else rule.subdomain for rule in rules)
rows = []

for rule in rules:
    row = [
        rule.endpoint,
        ", ".join(sorted((rule.methods or set()) - ignored_methods)),
    ]

    if has_domain:
        row.append((rule.host if host_matching else rule.subdomain) or "")

    row.append(rule.rule)
    rows.append(row)

headers = ["Endpoint", "Methods"]
sorts = ["endpoint", "methods"]

if has_domain:
    headers.append("Host" if host_matching else "Subdomain")
    sorts.append("domain")

headers.append("Rule")
sorts.append("rule")

try:
    rows.sort(key=itemgetter(sorts.index(sort)))
except ValueError:
    pass

rows.insert(0, headers)
widths = [max(len(row[i]) for row in rows) for i in range(len(headers))]
rows.insert(1, ["-" * w for w in widths])
template = "  ".join(f"{{{i}:<{w}}}" for i, w in enumerate(widths))

for row in rows:
    click.echo(template.format(*row))
