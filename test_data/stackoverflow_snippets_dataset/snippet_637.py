# Extracted from https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
from django.http import HttpResponse
import json

class JsonResponse(HttpResponse):
    def __init__(self, content={}, mimetype=None, status=None,
             content_type='application/json'):
        super(JsonResponse, self).__init__(json.dumps(content), mimetype=mimetype,
                                           status=status, content_type=content_type)

resp_data = {'my_key': 'my value',}
return JsonResponse(resp_data)

