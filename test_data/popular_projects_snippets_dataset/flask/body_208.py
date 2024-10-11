# Extracted from ./data/repos/flask/src/flask/scaffold.py
"""Alternative error attach function to the :meth:`errorhandler`
        decorator that is more straightforward to use for non decorator
        usage.

        .. versionadded:: 0.7
        """
exc_class, code = self._get_exc_class_and_code(code_or_exception)
self.error_handler_spec[None][code][exc_class] = f
