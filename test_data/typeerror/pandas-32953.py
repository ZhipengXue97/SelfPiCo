for obj in objs:
    if not isinstance(obj, (Series, DataFrame)):
        msg = (
            f"cannot concatenate object of type '{type(obj)}'; "
            "only Series and DataFrame objs are valid"
        )
        raise TypeError(msg)