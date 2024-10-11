# Extracted from ./data/repos/flask/src/flask/templating.py
"""Render a template by name with the given context as a stream.
    This returns an iterator of strings, which can be used as a
    streaming response from a view.

    :param template_name_or_list: The name of the template to render. If
        a list is given, the first name to exist will be rendered.
    :param context: The variables to make available in the template.

    .. versionadded:: 2.2
    """
app = current_app._get_current_object()  # type: ignore[attr-defined]
template = app.jinja_env.get_or_select_template(template_name_or_list)
exit(_stream(app, template, context))
