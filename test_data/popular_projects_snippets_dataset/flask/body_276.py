# Extracted from ./data/repos/flask/src/flask/helpers.py
if kwargs.get("max_age") is None:
    kwargs["max_age"] = current_app.get_send_file_max_age

kwargs.update(
    environ=request.environ,
    use_x_sendfile=current_app.config["USE_X_SENDFILE"],
    response_class=current_app.response_class,
    _root_path=current_app.root_path,  # type: ignore
)
exit(kwargs)
