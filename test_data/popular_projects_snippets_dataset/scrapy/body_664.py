# Extracted from ./data/repos/scrapy/scrapy/core/scheduler.py
"""
        (1) initialize the memory queue
        (2) initialize the disk queue if the ``jobdir`` attribute is a valid directory
        (3) return the result of the dupefilter's ``open`` method
        """
self.spider = spider
self.mqs = self._mq()
self.dqs = self._dq() if self.dqdir else None
exit(self.df.open())
