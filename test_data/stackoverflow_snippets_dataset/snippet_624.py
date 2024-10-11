# Extracted from https://stackoverflow.com/questions/16573332/jsondecodeerror-expecting-value-line-1-column-1-char-0
with open("text.json") as file:
    data=file.read()
    json_dict=json.load(file)

with open("text.json") as file:
   data=file.read()
   json_dict=json.loads(data)

