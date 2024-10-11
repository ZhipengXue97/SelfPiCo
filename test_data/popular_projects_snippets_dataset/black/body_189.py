# Extracted from ./data/repos/black/src/black/cache.py
"""Update the cache file."""
cache_file = get_cache_file(mode)
try:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    new_cache = {
        **cache,
        **{str(src.resolve()): get_cache_info(src) for src in sources},
    }
    with tempfile.NamedTemporaryFile(dir=str(cache_file.parent), delete=False) as f:
        pickle.dump(new_cache, f, protocol=4)
    os.replace(f.name, cache_file)
except OSError:
    pass
