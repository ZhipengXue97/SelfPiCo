# Extracted from ./data/repos/scrapy/scrapy/pqueues.py
priority = self.priority(request)
if priority not in self.queues:
    self.queues[priority] = self.qfactory(priority)
q = self.queues[priority]
q.push(request)  # this may fail (eg. serialization error)
if self.curprio is None or priority < self.curprio:
    self.curprio = priority
