# Extracted from ./data/repos/flask/src/flask/testing.py
"""Invokes a CLI command in an isolated environment. See
        :meth:`CliRunner.invoke <click.testing.CliRunner.invoke>` for
        full method documentation. See :ref:`testing-cli` for examples.

        If the ``obj`` argument is not given, passes an instance of
        :class:`~flask.cli.ScriptInfo` that knows how to load the Flask
        app being tested.

        :param cli: Command object to invoke. Default is the app's
            :attr:`~flask.app.Flask.cli` group.
        :param args: List of strings to invoke the command with.

        :return: a :class:`~click.testing.Result` object.
        """
if cli is None:
    cli = self.app.cli  # type: ignore

if "obj" not in kwargs:
    kwargs["obj"] = ScriptInfo(create_app=lambda: self.app)

exit(super().invoke(cli, args, **kwargs))
