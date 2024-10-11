# Extracted from https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
temp_dict = {}
exec("temp_dict['val'] = 10") 
print(temp_dict['val'])

