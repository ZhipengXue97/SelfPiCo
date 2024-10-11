# Extracted from https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask

from flask import request

@app.route('/my-route', methods=['POST'])
# you should always parse username and 
# password in a POST method not GET
def my_route():
    username = request.form.get("user_name")
    print(username)
    password = request.form.get("password")
    print(password)
    #now manipulate the username and password variables as you wish
    #Tip: define another method instead of methods=['GET','POST'], if you want to  
    # render the same template with a GET request too

