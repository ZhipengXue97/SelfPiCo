# Extracted from ./data/repos/flask/src/flask/app.py
super().__init__(
    import_name=import_name,
    static_folder=static_folder,
    static_url_path=static_url_path,
    template_folder=template_folder,
    root_path=root_path,
)

if instance_path is None:
    instance_path = self.auto_find_instance_path()
elif not os.path.isabs(instance_path):
    raise ValueError(
        "If an instance path is provided it must be absolute."
        " A relative path was given instead."
    )

#: Holds the path to the instance folder.
#:
#: .. versionadded:: 0.8
self.instance_path = instance_path

#: The configuration dictionary as :class:`Config`.  This behaves
#: exactly like a regular dictionary but supports additional methods
#: to load a config from files.
self.config = self.make_config(instance_relative_config)

#: An instance of :attr:`aborter_class` created by
#: :meth:`make_aborter`. This is called by :func:`flask.abort`
#: to raise HTTP errors, and can be called directly as well.
#:
#: .. versionadded:: 2.2
#:     Moved from ``flask.abort``, which calls this object.
self.aborter = self.make_aborter()

self.json: JSONProvider = self.json_provider_class(self)
"""Provides access to JSON methods. Functions in ``flask.json``
        will call methods on this provider when the application context
        is active. Used for handling JSON requests and responses.

        An instance of :attr:`json_provider_class`. Can be customized by
        changing that attribute on a subclass, or by assigning to this
        attribute afterwards.

        The default, :class:`~flask.json.provider.DefaultJSONProvider`,
        uses Python's built-in :mod:`json` library. A different provider
        can use a different JSON library.

        .. versionadded:: 2.2
        """

#: A list of functions that are called by
#: :meth:`handle_url_build_error` when :meth:`.url_for` raises a
#: :exc:`~werkzeug.routing.BuildError`. Each function is called
#: with ``error``, ``endpoint`` and ``values``. If a function
#: returns ``None`` or raises a ``BuildError``, it is skipped.
#: Otherwise, its return value is returned by ``url_for``.
#:
#: .. versionadded:: 0.9
self.url_build_error_handlers: list[
    t.Callable[[Exception, str, dict[str, t.Any]], str]
] = []

#: A list of functions that are called when the application context
#: is destroyed.  Since the application context is also torn down
#: if the request ends this is the place to store code that disconnects
#: from databases.
#:
#: .. versionadded:: 0.9
self.teardown_appcontext_funcs: list[ft.TeardownCallable] = []

#: A list of shell context processor functions that should be run
#: when a shell context is created.
#:
#: .. versionadded:: 0.11
self.shell_context_processors: list[ft.ShellContextProcessorCallable] = []

#: Maps registered blueprint names to blueprint objects. The
#: dict retains the order the blueprints were registered in.
#: Blueprints can be registered multiple times, this dict does
#: not track how often they were attached.
#:
#: .. versionadded:: 0.7
self.blueprints: dict[str, Blueprint] = {}

#: a place where extensions can store application specific state.  For
#: example this is where an extension could store database engines and
#: similar things.
#:
#: The key must match the name of the extension module. For example in
#: case of a "Flask-Foo" extension in `flask_foo`, the key would be
#: ``'foo'``.
#:
#: .. versionadded:: 0.7
self.extensions: dict = {}

#: The :class:`~werkzeug.routing.Map` for this instance.  You can use
#: this to change the routing converters after the class was created
#: but before any routes are connected.  Example::
#:
#:    from werkzeug.routing import BaseConverter
#:
#:    class ListConverter(BaseConverter):
#:        def to_python(self, value):
#:            return value.split(',')
#:        def to_url(self, values):
#:            return ','.join(super(ListConverter, self).to_url(value)
#:                            for value in values)
#:
#:    app = Flask(__name__)
#:    app.url_map.converters['list'] = ListConverter
self.url_map = self.url_map_class()

self.url_map.host_matching = host_matching
self.subdomain_matching = subdomain_matching

# tracks internally if the application already handled at least one
# request.
self._got_first_request = False

# Add a static route using the provided static_url_path, static_host,
# and static_folder if there is a configured static_folder.
# Note we do this without checking if static_folder exists.
# For one, it might be created while the server is running (e.g. during
# development). Also, Google App Engine stores static files somewhere
if self.has_static_folder:
    assert (
        bool(static_host) == host_matching
    ), "Invalid static_host/host_matching combination"
    # Use a weakref to avoid creating a reference cycle between the app
    # and the view function (see #3761).
    self_ref = weakref.ref(self)
    self.add_url_rule(
        f"{self.static_url_path}/<path:filename>",
        endpoint="static",
        host=static_host,
        view_func=lambda **kw: self_ref().send_static_file(**kw),  # type: ignore # noqa: B950
    )

# Set the name of the Click group in case someone wants to add
# the app's commands to another CLI tool.
self.cli.name = self.name
