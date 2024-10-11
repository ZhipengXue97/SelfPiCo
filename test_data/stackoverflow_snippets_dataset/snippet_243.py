# Extracted from https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
headers = {"charset": "utf-8", "Content-Type": "application/json"}
url = 'http://localhost:PORT_NUM/FILE.php'

r = requests.post(url, json=YOUR_JSON_DATA, headers=headers)
print(r.text)

