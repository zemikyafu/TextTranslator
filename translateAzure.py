import requests, uuid

class translateAzure:
    
    def translateWithAzure (fromLang,toLang,text):
      
        key = ""
        endpoint = ""
        location = "eastus2"


        path = '/translate'
        constructed_url = endpoint + path
        params = {
            'api-version': 3.0,
            'from': fromLang,
            'to': toLang
        }
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{
            'text': text
        }]
        response = requests.post(constructed_url, params=params, headers=headers, json=body)
        return response