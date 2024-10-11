# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
out = feed.copy()
out.setdefault("batch_item_count", settings.getint("FEED_EXPORT_BATCH_ITEM_COUNT"))
out.setdefault("encoding", settings["FEED_EXPORT_ENCODING"])
out.setdefault("fields", settings.getdictorlist("FEED_EXPORT_FIELDS") or None)
out.setdefault("store_empty", settings.getbool("FEED_STORE_EMPTY"))
out.setdefault("uri_params", settings["FEED_URI_PARAMS"])
out.setdefault("item_export_kwargs", {})
if settings["FEED_EXPORT_INDENT"] is None:
    out.setdefault("indent", None)
else:
    out.setdefault("indent", settings.getint("FEED_EXPORT_INDENT"))
exit(out)
