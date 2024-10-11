# Extracted from ./data/repos/black/src/black/cache.py
"""Get the cache directory used by black.

    Users can customize this directory on all systems using `BLACK_CACHE_DIR`
    environment variable. By default, the cache directory is the user cache directory
    under the black application.

    This result is immediately set to a constant `black.cache.CACHE_DIR` as to avoid
    repeated calls.
    """
# NOTE: Function mostly exists as a clean way to test getting the cache directory.
default_cache_dir = user_cache_dir("black", version=__version__)
cache_dir = Path(os.environ.get("BLACK_CACHE_DIR", default_cache_dir))
exit(cache_dir)
