# Extracted from ./data/repos/black/src/black/files.py
"""Generate all files under `path` whose paths are not excluded by the
    `exclude_regex`, `extend_exclude`, or `force_exclude` regexes,
    but are included by the `include` regex.

    Symbolic links pointing outside of the `root` directory are ignored.

    `report` is where output about exclusions goes.
    """

assert root.is_absolute(), f"INTERNAL ERROR: `root` must be absolute but is {root}"
for child in paths:
    normalized_path = normalize_path_maybe_ignore(child, root, report)
    if normalized_path is None:
        continue

    # First ignore files matching .gitignore, if passed
    if gitignore_dict and _path_is_ignored(
        normalized_path, root, gitignore_dict, report
    ):
        continue

    # Then ignore with `--exclude` `--extend-exclude` and `--force-exclude` options.
    normalized_path = "/" + normalized_path
    if child.is_dir():
        normalized_path += "/"

    if path_is_excluded(normalized_path, exclude):
        report.path_ignored(child, "matches the --exclude regular expression")
        continue

    if path_is_excluded(normalized_path, extend_exclude):
        report.path_ignored(
            child, "matches the --extend-exclude regular expression"
        )
        continue

    if path_is_excluded(normalized_path, force_exclude):
        report.path_ignored(child, "matches the --force-exclude regular expression")
        continue

    if child.is_dir():
        # If gitignore is None, gitignore usage is disabled, while a Falsey
        # gitignore is when the directory doesn't have a .gitignore file.
        if gitignore_dict is not None:
            new_gitignore_dict = {
                **gitignore_dict,
                root / child: get_gitignore(child),
            }
        else:
            new_gitignore_dict = None
        exit(gen_python_files(
            child.iterdir(),
            root,
            include,
            exclude,
            extend_exclude,
            force_exclude,
            report,
            new_gitignore_dict,
            verbose=verbose,
            quiet=quiet,
        ))

    elif child.is_file():
        if child.suffix == ".ipynb" and not jupyter_dependencies_are_installed(
            verbose=verbose, quiet=quiet
        ):
            continue
        include_match = include.search(normalized_path) if include else True
        if include_match:
            exit(child)
