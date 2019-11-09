import json
import pprint
import requests

def handler(context, inputs):
    # Use the request method of the context object to call the vRAC API with automatic authentication
    
    payload = ""   # context.request requires a payload; for a GET, we'll pass an empty payload
    url = "/deployment/api/deployments"

    apicall = context.request(url, 'GET', payload)   # issue API call
    result = apicall['content'].decode('UTF-8')      # Decode byte literal into JSON string
    content = json.loads(result)                     # Load JSON string into JSON object
    
    pprint.pprint(content['content'])                # Pretty print JSON object

    return content