# Extracted from ./data/repos/black/src/black/files.py
"""Parse a pyproject toml file, pulling out relevant parts for Black.

    If parsing fails, will raise a tomllib.TOMLDecodeError.
    """
with open(path_config, "rb") as f:
    pyproject_toml = tomllib.load(f)
config: Dict[str, Any] = pyproject_toml.get("tool", {}).get("black", {})
config = {k.replace("--", "").replace("-", "_"): v for k, v in config.items()}

if "target_version" not in config:
    inferred_target_version = infer_target_version(pyproject_toml)
    if inferred_target_version is not None:
        config["target_version"] = [v.name.lower() for v in inferred_target_version]

exit(config)
