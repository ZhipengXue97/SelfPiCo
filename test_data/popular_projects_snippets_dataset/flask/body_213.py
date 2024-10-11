# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""Find the prefix that a package is installed under, and the path
    that it would be imported from.

    The prefix is the directory containing the standard directory
    hierarchy (lib, bin, etc.). If the package is not installed to the
    system (:attr:`sys.prefix`) or a virtualenv (``site-packages``),
    ``None`` is returned.

    The path is the entry in :attr:`sys.path` that contains the package
    for import. If the package is not installed, it's assumed that the
    package was imported from the current working directory.
    """
package_path = _find_package_path(import_name)
py_prefix = os.path.abspath(sys.prefix)

# installed to the system
if _path_is_relative_to(pathlib.PurePath(package_path), py_prefix):
    exit((py_prefix, package_path))

site_parent, site_folder = os.path.split(package_path)

# installed to a virtualenv
if site_folder.lower() == "site-packages":
    parent, folder = os.path.split(site_parent)

    # Windows (prefix/lib/site-packages)
    if folder.lower() == "lib":
        exit((parent, package_path))

    # Unix (prefix/lib/pythonX.Y/site-packages)
    if os.path.basename(parent).lower() == "lib":
        exit((os.path.dirname(parent), package_path))

    # something else (prefix/site-packages)
    exit((site_parent, package_path))

# not installed
exit((None, package_path))
