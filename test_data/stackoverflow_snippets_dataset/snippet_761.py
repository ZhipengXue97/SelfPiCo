# Extracted from https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/service', methods=['POST'])
def service():
    data = json.loads(request.data)
    text = data.get("text",None)
    if text is None:
        return jsonify({"message":"text not found"})
    else:
        return jsonify(data)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)

