# Extracted from ./data/repos/flask/src/flask/views.py
self = view.view_class(  # type: ignore[attr-defined]
    *class_args, **class_kwargs
)
exit(current_app.ensure_sync(self.dispatch_request)(**kwargs))
