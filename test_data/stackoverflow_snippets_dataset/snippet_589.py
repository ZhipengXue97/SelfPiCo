# Extracted from https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
from threading import Thread as _Thread


class ThreadWrapper:
    def __init__(self, target, *args, **kwargs):
        self.result = None
        self._target = self._build_threaded_fn(target)
        self.thread = _Thread(
            target=self._target,
            *args,
            **kwargs
        )

    def _build_threaded_fn(self, func):
        def inner(*args, **kwargs):
            self.result = func(*args, **kwargs)
        return inner


import time
from commons import ThreadWrapper


def test():

    def target():
        time.sleep(1)
        return 'Hello'

    wrapper = ThreadWrapper(target=target)
    wrapper.thread.start()

    r = wrapper.result
    assert r is None

    time.sleep(2)

    r = wrapper.result
    assert r == 'Hello'

