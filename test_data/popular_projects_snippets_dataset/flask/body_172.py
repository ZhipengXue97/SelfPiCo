# Extracted from ./data/repos/flask/src/flask/views.py
"""Convert the class into a view function that can be registered
        for a route.

        By default, the generated view will create a new instance of the
        view class for every request and call its
        :meth:`dispatch_request` method. If the view class sets
        :attr:`init_every_request` to ``False``, the same instance will
        be used for every request.

        Except for ``name``, all other arguments passed to this method
        are forwarded to the view class ``__init__`` method.

        .. versionchanged:: 2.2
            Added the ``init_every_request`` class attribute.
        """
if cls.init_every_request:

    def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
        self = view.view_class(  # type: ignore[attr-defined]
            *class_args, **class_kwargs
        )
        exit(current_app.ensure_sync(self.dispatch_request)(**kwargs))

else:
    self = cls(*class_args, **class_kwargs)

    def view(**kwargs: t.Any) -> ft.ResponseReturnValue:
        exit(current_app.ensure_sync(self.dispatch_request)(**kwargs))

if cls.decorators:
    view.__name__ = name
    view.__module__ = cls.__module__
    for decorator in cls.decorators:
        view = decorator(view)

# We attach the view class to the view function for two reasons:
# first of all it allows us to easily figure out what class-based
# view this thing came from, secondly it's also used for instantiating
# the view class so you can actually replace it with something else
# for testing purposes and debugging.
view.view_class = cls  # type: ignore
view.__name__ = name
view.__doc__ = cls.__doc__
view.__module__ = cls.__module__
view.methods = cls.methods  # type: ignore
view.provide_automatic_options = cls.provide_automatic_options  # type: ignore
exit(view)
