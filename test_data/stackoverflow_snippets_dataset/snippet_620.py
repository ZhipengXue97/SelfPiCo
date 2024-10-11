# Extracted from https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
from datetime import date, timedelta, datetime

class DateRange:
    def __init__(self, start, end, step=timedelta(1)):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        start = self.start
        step = self.step
        end = self.end

        n = int((end - start) / step)
        d = start

        for _ in range(n):
            yield d
            d += step

    def __contains__(self, value):
        return (
            (self.start <= value < self.end) and 
            ((value - self.start) % self.step == timedelta(0))
        )

