# Extracted from ./data/repos/flask/src/flask/app.py
"""Given the return value from a view function this finalizes
        the request by converting it into a response and invoking the
        postprocessing functions.  This is invoked for both normal
        request dispatching as well as error handlers.

        Because this means that it might be called as a result of a
        failure a special safe mode is available which can be enabled
        with the `from_error_handler` flag.  If enabled, failures in
        response processing will be logged and otherwise ignored.

        :internal:
        """
response = self.make_response(rv)
try:
    response = self.process_response(response)
    request_finished.send(
        self, _async_wrapper=self.ensure_sync, response=response
    )
except Exception:
    if not from_error_handler:
        raise
    self.logger.exception(
        "Request finalizing failed with an error while handling an error"
    )
exit(response)
