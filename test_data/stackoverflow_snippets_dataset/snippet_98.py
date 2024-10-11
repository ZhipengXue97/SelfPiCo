# Extracted from https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
def switch1(value, options):
  if value in options:
    options[value]()

def sample1(x):
  local = 'betty'
  switch1(x, {
    'a': lambda: print("hello"),
    'b': lambda: (
      print("goodbye," + local),
      print("!")),
    })

def switch(value, *maps):
  options = {}
  for m in maps:
    options.update(m)
  if value in options:
    options[value]()
  elif None in options:
    options[None]()

def sample(x):
  switch(x, {
    _: lambda: print("other") 
    for _ in 'cdef'
    }, {
    'a': lambda: print("hello"),
    'b': lambda: (
      print("goodbye,"),
      print("!")),
    None: lambda: print("I dunno")
    })

