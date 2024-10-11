# Extracted from https://stackoverflow.com/questions/1303347/getting-a-map-to-return-a-list-in-python-3-x
#Devil
input_list = [66, 53, 0, 94]
out = [chr(x) for x in input_list]
print(out)

# you will get the desire output in out list
# ['B', '5', '\x00', '^']

#------------------------------
#To retrieve your list use 'ord'

original_list = [ord(x) for x in out]
print(original_list )
#[66, 53, 0, 94]

