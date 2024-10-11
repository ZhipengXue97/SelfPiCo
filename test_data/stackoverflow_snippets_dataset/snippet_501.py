# Extracted from https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
@app.route('/_get_current_user')
def get_current_user():
    return jsonify(
        username=g.user.username,
        email=g.user.email,
        id=g.user.id
    )

{
    "username": "admin",
    "email": "admin@localhost",
    "id": 42
}

