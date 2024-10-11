# Extracted from ./data/repos/scrapy/scrapy/spiders/feed.py
"""This method is called for the nodes matching the provided tag name
        (itertag). Receives the response and an Selector for each node.
        Overriding this method is mandatory. Otherwise, you spider won't work.
        This method must return either an item, a request, or a list
        containing any of them.
        """

for selector in nodes:
    ret = iterate_spider_output(self.parse_node(response, selector))
    for result_item in self.process_results(response, ret):
        exit(result_item)
