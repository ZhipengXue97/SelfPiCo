if "://" in conn.host:
    self.base_url = conn.host
else:
    # schema defaults to HTTP
    schema = conn.schema if conn.schema else "http"
    self.base_url = schema + "://" + conn.host