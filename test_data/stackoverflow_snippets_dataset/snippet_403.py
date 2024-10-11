# Extracted from https://stackoverflow.com/questions/518021/is-arr-len-the-preferred-way-to-get-the-length-of-an-array-in-python
my_list = [1,2,3,4,5]
len(my_list)
# 5

my_tuple = (1,2,3,4,5)
len(my_tuple)
# 5

my_string = 'hello world'
len(my_string)
# 11

lengths = map(len, list_of_containers)

