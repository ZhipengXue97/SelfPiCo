# Extracted from ./data/repos/scrapy/scrapy/spiderloader.py
dupes = []
for name, locations in self._found.items():
    dupes.extend(
        [
            f"  {cls} named {name!r} (in {mod})"
            for mod, cls in locations
            if len(locations) > 1
        ]
    )

if dupes:
    dupes_string = "\n\n".join(dupes)
    warnings.warn(
        "There are several spiders with the same name:\n\n"
        f"{dupes_string}\n\n  This can cause unexpected behavior.",
        category=UserWarning,
    )
