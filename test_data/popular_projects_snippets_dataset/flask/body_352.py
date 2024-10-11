# Extracted from ./data/repos/flask/src/flask/cli.py
"""Run a local development server.

    This server is for development purposes only. It does not provide
    the stability, security, or performance of production WSGI servers.

    The reloader and debugger are enabled by default with the '--debug'
    option.
    """
try:
    app = info.load_app()
except Exception as e:
    if is_running_from_reloader():
        # When reloading, print out the error immediately, but raise
        # it later so the debugger or server can handle it.
        traceback.print_exc()
        err = e

        def app(environ, start_response):
            raise err from None

    else:
        # When not reloading, raise the error immediately so the
        # command fails.
        raise e from None

debug = get_debug_flag()

if reload is None:
    reload = debug

if debugger is None:
    debugger = debug

show_server_banner(debug, info.app_import_path)

run_simple(
    host,
    port,
    app,
    use_reloader=reload,
    use_debugger=debugger,
    threaded=with_threads,
    ssl_context=cert,
    extra_files=extra_files,
    exclude_patterns=exclude_patterns,
)
