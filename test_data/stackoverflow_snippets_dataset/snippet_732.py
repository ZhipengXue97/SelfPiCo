# Extracted from https://stackoverflow.com/questions/100210/what-is-the-standard-way-to-add-n-seconds-to-datetime-time-in-python
sometime = arrow.now()
abitlater = sometime.shift(seconds=3)

