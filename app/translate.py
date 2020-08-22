import json
import requests,uuid
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
            'Ocp-Apim-Subscription-Region':'canadacentral',
            'Content-type': 'application/json; charset=UTF-8',
            'X-ClientTraceId': str(uuid.uuid4())
           }
    #print(text)
    body=[{'text':text}]
    #print(auth)
    #print(body)
    #print(app.config['MS_TRANSLATOR_KEY'])
    url='https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(
                         source_language, dest_language)
    #print(url)
    r = requests.post(url,headers=auth,json=body) # its was get
    if r.status_code != 200:
        print(r.status_code)
        return _('Error: the translation service failed.')
    #print(r.content)
    #print(r.content.decode('utf-8-sig'))
    #print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))

    return json.loads(r.content.decode('utf-8-sig'))[0]["translations"][0]["text"]
    #print(r.json())
    #return json.loads(r.json())
