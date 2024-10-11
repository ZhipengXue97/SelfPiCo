# Extracted from ./data/repos/flask/src/flask/json/tag.py
"""Register a new tag with this serializer.

        :param tag_class: tag class to register. Will be instantiated with this
            serializer instance.
        :param force: overwrite an existing tag. If false (default), a
            :exc:`KeyError` is raised.
        :param index: index to insert the new tag in the tag order. Useful when
            the new tag is a special case of an existing tag. If ``None``
            (default), the tag is appended to the end of the order.

        :raise KeyError: if the tag key is already registered and ``force`` is
            not true.
        """
tag = tag_class(self)
key = tag.key

if key is not None:
    if not force and key in self.tags:
        raise KeyError(f"Tag '{key}' is already registered.")

    self.tags[key] = tag

if index is None:
    self.order.append(tag)
else:
    self.order.insert(index, tag)
