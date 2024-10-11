# Extracted from https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
data = request.get_json()
name = data.get('name', '')

name = request.form.get('name', '')

request.args.get("name", "")

