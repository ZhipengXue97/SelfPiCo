# Extracted from ./data/repos/scrapy/scrapy/core/engine.py
self.closing: Optional[Deferred] = None
self.inprogress: Set[Request] = set()
self.start_requests: Optional[Iterator[Request]] = iter(start_requests)
self.close_if_idle: bool = close_if_idle
self.nextcall: CallLaterOnce = nextcall
self.scheduler: "BaseScheduler" = scheduler
self.heartbeat: LoopingCall = LoopingCall(nextcall.schedule)
