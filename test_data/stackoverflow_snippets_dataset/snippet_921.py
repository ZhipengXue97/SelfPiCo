# Extracted from https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
d = {"name":"interpolator",
     "children":[{'name':key,"size":value} for key,value in sample.items()]}
json_string = json.dumps(d)

