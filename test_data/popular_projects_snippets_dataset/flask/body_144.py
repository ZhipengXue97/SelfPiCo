# Extracted from ./data/repos/flask/src/flask/app.py
"""Handle an exception that did not have an error handler
        associated with it, or that was raised from an error handler.
        This always causes a 500 ``InternalServerError``.

        Always sends the :data:`got_request_exception` signal.

        If :data:`PROPAGATE_EXCEPTIONS` is ``True``, such as in debug
        mode, the error will be re-raised so that the debugger can
        display it. Otherwise, the original exception is logged, and
        an :exc:`~werkzeug.exceptions.InternalServerError` is returned.

        If an error handler is registered for ``InternalServerError`` or
        ``500``, it will be used. For consistency, the handler will
        always receive the ``InternalServerError``. The original
        unhandled exception is available as ``e.original_exception``.

        .. versionchanged:: 1.1.0
            Always passes the ``InternalServerError`` instance to the
            handler, setting ``original_exception`` to the unhandled
            error.

        .. versionchanged:: 1.1.0
            ``after_request`` functions and other finalization is done
            even for the default 500 response when there is no handler.

        .. versionadded:: 0.3
        """
exc_info = sys.exc_info()
got_request_exception.send(self, _async_wrapper=self.ensure_sync, exception=e)
propagate = self.config["PROPAGATE_EXCEPTIONS"]

if propagate is None:
    propagate = self.testing or self.debug

if propagate:
    # Re-raise if called with an active exception, otherwise
    # raise the passed in exception.
    if exc_info[1] is e:
        raise

    raise e

self.log_exception(exc_info)
server_error: InternalServerError | ft.ResponseReturnValue
server_error = InternalServerError(original_exception=e)
handler = self._find_error_handler(server_error)

if handler is not None:
    server_error = self.ensure_sync(handler)(server_error)

exit(self.finalize_request(server_error, from_error_handler=True))
