from flask import Flask, request
import config
import json
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cucumber', methods=['GET', 'POST'])
def cucumber():
    freq = request.args['f']
    if (freq == 'yo'):
        return yo()
    elif (freq == 'venmo'):
        return venmo()
    return freq

def yo():
    yo_all_request = requests.post("http://api.justyo.co/yoall/", data={'api_token': config.YO_API_TOKEN})
    if 'result' in yo_all_request.json() and yo_all_request.json()['result'] == 'OK':
        return json.dumps({'text': 'Yo sent to all!'})
    else:
        return json.dumps({'text': 'Error sending Yo. API may be down...'})

    return str(keys['yo_access_token'])
      
def venmo():
    pay = {}
    pay['access_token'] = config.VENMO_API_TOKEN
    pay['email'] = config.venmo_email
    pay['note'] = 'test'
    pay['amount'] = 0.02
    url = 'https://api.venmo.com/v1/payments'
    resp = requests.post(url, pay)

    return str(resp.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
