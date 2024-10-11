# Extracted from https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
{
  "old_key_name": "new_key_name",
  "old_key_name_2": "new_key_name_2",
}

with open("<filepath>") as json_file:
    format_dict = json.load(json_file)

def format_output(dict_to_format,format_dict):
  for row in dict_to_format:
    if row in format_dict.keys() and row != format_dict[row]:
      dict_to_format[format_dict[row]] = dict_to_format.pop(row)
  return dict_to_format

