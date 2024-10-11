# Extracted from https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
import requests

url = 'https://www.python.org/static/img/python-logo.png'
fileName = 'D:\Python\dwnldPythonLogo.png'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()

