# Extracted from ./data/repos/flask/src/flask/templating.py
exit(template.generate(context))
template_rendered.send(
    app, _async_wrapper=app.ensure_sync, template=template, context=context
)
