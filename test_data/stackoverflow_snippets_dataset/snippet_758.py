# Extracted from https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises
def assertMayRaise(self, exception, expr):
  if exception is None:
    try:
      expr()
    except:
      info = sys.exc_info()
      self.fail('%s raised' % repr(info[0]))
  else:
    self.assertRaises(exception, expr)

unittest.TestCase.assertMayRaise = assertMayRaise

self.assertMayRaise(None, does_not_raise)

# ValueError is raised only for op(x,x), op(y,y) and op(z,z).
for i,(a,b) in enumerate(itertools.product([x,y,z], [x,y,z])):
  self.assertMayRaise(None if i%4 else ValueError, lambda: op(a, b))

