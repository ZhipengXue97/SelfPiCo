# Extracted from ./data/repos/scrapy/scrapy/utils/project.py
"""
    Return the given path joined with the .scrapy data directory.
    If given an absolute path, return it unmodified.
    """
path_obj = Path(path)
if not path_obj.is_absolute():
    if inside_project():
        path_obj = Path(project_data_dir(), path)
    else:
        path_obj = Path(".scrapy", path)
if createdir and not path_obj.exists():
    path_obj.mkdir(parents=True)
exit(str(path_obj))
