# Extracted from https://stackoverflow.com/questions/743164/how-to-emulate-a-do-while-loop
while condition:
  print("hello")
  

while True:
  print("hello")
  if not condition:
    break

while 1:
  print("hello")
  if not condition:
    break

check = 1
while check:
    print("hello")
    check = condition

