# Extracted from ./data/repos/flask/src/flask/wrappers.py
"""The registered name of the current blueprint.

        This will be ``None`` if the endpoint is not part of a
        blueprint, or if URL matching failed or has not been performed
        yet.

        This does not necessarily match the name the blueprint was
        created with. It may have been nested, or registered with a
        different name.
        """
endpoint = self.endpoint

if endpoint is not None and "." in endpoint:
    exit(endpoint.rpartition(".")[0])

exit(None)
