# Extracted from ./data/repos/black/src/black/__init__.py
"""Compute the set of files to be formatted."""
sources: Set[Path] = set()
root = ctx.obj["root"]

using_default_exclude = exclude is None
exclude = re_compile_maybe_verbose(DEFAULT_EXCLUDES) if exclude is None else exclude
gitignore: Optional[Dict[Path, PathSpec]] = None
root_gitignore = get_gitignore(root)

for s in src:
    if s == "-" and stdin_filename:
        p = Path(stdin_filename)
        is_stdin = True
    else:
        p = Path(s)
        is_stdin = False

    if is_stdin or p.is_file():
        normalized_path: Optional[str] = normalize_path_maybe_ignore(
            p, ctx.obj["root"], report
        )
        if normalized_path is None:
            if verbose:
                out(f'Skipping invalid source: "{normalized_path}"', fg="red")
            continue
        if verbose:
            out(f'Found input source: "{normalized_path}"', fg="blue")

        normalized_path = "/" + normalized_path
        # Hard-exclude any files that matches the `--force-exclude` regex.
        if force_exclude:
            force_exclude_match = force_exclude.search(normalized_path)
        else:
            force_exclude_match = None
        if force_exclude_match and force_exclude_match.group(0):
            report.path_ignored(p, "matches the --force-exclude regular expression")
            continue

        if is_stdin:
            p = Path(f"{STDIN_PLACEHOLDER}{str(p)}")

        if p.suffix == ".ipynb" and not jupyter_dependencies_are_installed(
            verbose=verbose, quiet=quiet
        ):
            continue

        sources.add(p)
    elif p.is_dir():
        p = root / normalize_path_maybe_ignore(p, ctx.obj["root"], report)
        if verbose:
            out(f'Found input source directory: "{p}"', fg="blue")

        if using_default_exclude:
            gitignore = {
                root: root_gitignore,
                p: get_gitignore(p),
            }
        sources.update(
            gen_python_files(
                p.iterdir(),
                ctx.obj["root"],
                include,
                exclude,
                extend_exclude,
                force_exclude,
                report,
                gitignore,
                verbose=verbose,
                quiet=quiet,
            )
        )
    elif s == "-":
        if verbose:
            out("Found input source stdin", fg="blue")
        sources.add(p)
    else:
        err(f"invalid path: {s}")

exit(sources)
