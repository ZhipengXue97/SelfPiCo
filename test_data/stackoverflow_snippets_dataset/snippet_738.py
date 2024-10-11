# Extracted from https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror
import requests

url = "Write your url here"

returnResponse = requests.get(url, verify=False)

