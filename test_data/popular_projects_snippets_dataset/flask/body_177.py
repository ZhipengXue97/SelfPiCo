# Extracted from ./data/repos/flask/src/flask/scaffold.py
#: The name of the package or module that this object belongs
#: to. Do not change this once it is set by the constructor.
self.import_name = import_name

self.static_folder = static_folder  # type: ignore
self.static_url_path = static_url_path

#: The path to the templates folder, relative to
#: :attr:`root_path`, to add to the template loader. ``None`` if
#: templates should not be added.
self.template_folder = template_folder

if root_path is None:
    root_path = get_root_path(self.import_name)

#: Absolute path to the package on the filesystem. Used to look
#: up resources contained in the package.
self.root_path = root_path

#: The Click command group for registering CLI commands for this
#: object. The commands are available from the ``flask`` command
#: once the application has been discovered and blueprints have
#: been registered.
self.cli = AppGroup()

#: A dictionary mapping endpoint names to view functions.
#:
#: To register a view function, use the :meth:`route` decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.view_functions: dict[str, t.Callable] = {}

#: A data structure of registered error handlers, in the format
#: ``{scope: {code: {class: handler}}}``. The ``scope`` key is
#: the name of a blueprint the handlers are active for, or
#: ``None`` for all requests. The ``code`` key is the HTTP
#: status code for ``HTTPException``, or ``None`` for
#: other exceptions. The innermost dictionary maps exception
#: classes to handler functions.
#:
#: To register an error handler, use the :meth:`errorhandler`
#: decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.error_handler_spec: dict[
    ft.AppOrBlueprintKey,
    dict[int | None, dict[type[Exception], ft.ErrorHandlerCallable]],
] = defaultdict(lambda: defaultdict(dict))

#: A data structure of functions to call at the beginning of
#: each request, in the format ``{scope: [functions]}``. The
#: ``scope`` key is the name of a blueprint the functions are
#: active for, or ``None`` for all requests.
#:
#: To register a function, use the :meth:`before_request`
#: decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.before_request_funcs: dict[
    ft.AppOrBlueprintKey, list[ft.BeforeRequestCallable]
] = defaultdict(list)

#: A data structure of functions to call at the end of each
#: request, in the format ``{scope: [functions]}``. The
#: ``scope`` key is the name of a blueprint the functions are
#: active for, or ``None`` for all requests.
#:
#: To register a function, use the :meth:`after_request`
#: decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.after_request_funcs: dict[
    ft.AppOrBlueprintKey, list[ft.AfterRequestCallable]
] = defaultdict(list)

#: A data structure of functions to call at the end of each
#: request even if an exception is raised, in the format
#: ``{scope: [functions]}``. The ``scope`` key is the name of a
#: blueprint the functions are active for, or ``None`` for all
#: requests.
#:
#: To register a function, use the :meth:`teardown_request`
#: decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.teardown_request_funcs: dict[
    ft.AppOrBlueprintKey, list[ft.TeardownCallable]
] = defaultdict(list)

#: A data structure of functions to call to pass extra context
#: values when rendering templates, in the format
#: ``{scope: [functions]}``. The ``scope`` key is the name of a
#: blueprint the functions are active for, or ``None`` for all
#: requests.
#:
#: To register a function, use the :meth:`context_processor`
#: decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.template_context_processors: dict[
    ft.AppOrBlueprintKey, list[ft.TemplateContextProcessorCallable]
] = defaultdict(list, {None: [_default_template_ctx_processor]})

#: A data structure of functions to call to modify the keyword
#: arguments passed to the view function, in the format
#: ``{scope: [functions]}``. The ``scope`` key is the name of a
#: blueprint the functions are active for, or ``None`` for all
#: requests.
#:
#: To register a function, use the
#: :meth:`url_value_preprocessor` decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.url_value_preprocessors: dict[
    ft.AppOrBlueprintKey,
    list[ft.URLValuePreprocessorCallable],
] = defaultdict(list)

#: A data structure of functions to call to modify the keyword
#: arguments when generating URLs, in the format
#: ``{scope: [functions]}``. The ``scope`` key is the name of a
#: blueprint the functions are active for, or ``None`` for all
#: requests.
#:
#: To register a function, use the :meth:`url_defaults`
#: decorator.
#:
#: This data structure is internal. It should not be modified
#: directly and its format may change at any time.
self.url_default_functions: dict[
    ft.AppOrBlueprintKey, list[ft.URLDefaultCallable]
] = defaultdict(list)
