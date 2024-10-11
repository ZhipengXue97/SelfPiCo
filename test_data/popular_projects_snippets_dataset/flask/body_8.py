# Extracted from ./data/repos/flask/src/flask/templating.py
app.update_template_context(context)
before_render_template.send(
    app, _async_wrapper=app.ensure_sync, template=template, context=context
)
rv = template.render(context)
template_rendered.send(
    app, _async_wrapper=app.ensure_sync, template=template, context=context
)
exit(rv)
