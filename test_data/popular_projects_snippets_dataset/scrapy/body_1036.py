# Extracted from ./data/repos/scrapy/scrapy/extensions/feedexport.py
slots = []
for slot in self.slots:
    if not slot.filter.accepts(item):
        slots.append(
            slot
        )  # if slot doesn't accept item, continue with next slot
        continue

    slot.start_exporting()
    slot.exporter.export_item(item)
    slot.itemcount += 1
    # create new slot for each slot with itemcount == FEED_EXPORT_BATCH_ITEM_COUNT and close the old one
    if (
        self.feeds[slot.uri_template]["batch_item_count"]
        and slot.itemcount >= self.feeds[slot.uri_template]["batch_item_count"]
    ):
        uri_params = self._get_uri_params(
            spider, self.feeds[slot.uri_template]["uri_params"], slot
        )
        self._close_slot(slot, spider)
        slots.append(
            self._start_new_batch(
                batch_id=slot.batch_id + 1,
                uri=slot.uri_template % uri_params,
                feed_options=self.feeds[slot.uri_template],
                spider=spider,
                uri_template=slot.uri_template,
            )
        )
    else:
        slots.append(slot)
self.slots = slots
