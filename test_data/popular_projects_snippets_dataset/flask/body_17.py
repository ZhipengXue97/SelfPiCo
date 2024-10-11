# Extracted from ./data/repos/flask/src/flask/testing.py
super().__init__(*args, **kwargs)
self.preserve_context = False
self._new_contexts: list[t.ContextManager[t.Any]] = []
self._context_stack = ExitStack()
self.environ_base = {
    "REMOTE_ADDR": "127.0.0.1",
    "HTTP_USER_AGENT": f"werkzeug/{werkzeug.__version__}",
}
