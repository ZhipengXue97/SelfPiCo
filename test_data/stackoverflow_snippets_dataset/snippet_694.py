# Extracted from https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def date_range(start, stop, step=1, inclusive=False):
    day_count = (stop - start).days
    if inclusive:
        day_count += 1

    if step > 0:
        range_args = (0, day_count, step)
    elif step < 0:
        range_args = (day_count - 1, -1, step)
    else:
        raise ValueError("date_range(): step arg must be non-zero")

    for i in range(*range_args):
        yield start + timedelta(days=i)

