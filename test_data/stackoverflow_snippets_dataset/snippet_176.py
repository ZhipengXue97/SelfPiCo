# Extracted from https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
# get json string
jsonStr = json.dumps(my_dictionary, indent=1, sort_keys=True, default=str)
# then covert json string to json object
return json.loads(jsonStr)

