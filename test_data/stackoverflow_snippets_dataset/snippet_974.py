# Extracted from https://stackoverflow.com/questions/4504662/why-does-rangestart-end-not-include-end
def main():
    for i in inclusive_range(25):
        print(i, sep=" ")


def inclusive_range(*args):
    numargs = len(args)
    if numargs == 0:
        raise TypeError("you need to write at least a value")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("Inclusive range was expected at most 3 arguments,got {}".format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__":
    main()

