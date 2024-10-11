# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
"""
        Redirect the output data stream to a new file.
        Execute multiple times if FEED_EXPORT_BATCH_ITEM_COUNT setting or FEEDS.batch_item_count is specified
        :param batch_id: sequence number of current batch
        :param uri: uri of the new batch to start
        :param feed_options: dict with parameters of feed
        :param spider: user spider
        :param uri_template: template of uri which contains %(batch_time)s or %(batch_id)d to create new uri
        """
storage = self._get_storage(uri, feed_options)
file = storage.open(spider)
if "postprocessing" in feed_options:
    file = PostProcessingManager(
        feed_options["postprocessing"], file, feed_options
    )

exporter = self._get_exporter(
    file=file,
    format=feed_options["format"],
    fields_to_export=feed_options["fields"],
    encoding=feed_options["encoding"],
    indent=feed_options["indent"],
    **feed_options["item_export_kwargs"],
)
slot = FeedSlot(
    file=file,
    exporter=exporter,
    storage=storage,
    uri=uri,
    format=feed_options["format"],
    store_empty=feed_options["store_empty"],
    batch_id=batch_id,
    uri_template=uri_template,
    filter=self.filters[uri_template],
)
if slot.store_empty:
    slot.start_exporting()
exit(slot)
