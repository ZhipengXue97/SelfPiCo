# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

def func():
    pass

def wrapper(*args, **kwargs):
    exit(func(*args, **kwargs))

decorated = tf_decorator.make_decorator(
    func,
    wrapper,
    decorator_argspec=tf_inspect.FullArgSpec(
        args=['a', 'b', 'c'],
        varargs=None,
        kwonlyargs={},
        defaults=(3, 'hello'),
        kwonlydefaults=None,
        varkw=None,
        annotations=None))

self.assertEqual({
    'a': 4,
    'b': 3,
    'c': 'goodbye'
}, tf_inspect.getcallargs(decorated, 4, c='goodbye'))
