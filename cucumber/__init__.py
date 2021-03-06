from flask import Flask, request
import config
import json
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cucumber')
def cucumber():
    return 'welcome to internet cucumber'

@app.route('/cucumber/yo')
def yo():
    yo_all_request = requests.post("http://api.justyo.co/yoall/", data={'api_token': config.YO_API_TOKEN})
    if 'result' in yo_all_request.json() and yo_all_request.json()['result'] == 'OK':
        return json.dumps({'text': 'Yo sent to all!'})
    else:
        return json.dumps({'text': 'Error sending Yo. API may be down...'})

@app.route('/cucumber/venmo')
def venmo():
    args = request.args
    cucumber_token = args['token']
    if (cucumber_token == config.cucumber_token):
      pay = {}
      pay['access_token'] = config.VENMO_API_TOKEN
      if args['to'] == 'teddy':
        pay['email'] = config.teddy_email
      elif args['to'] == 'nathan':
        pay['email'] = config.nathan_email
      elif args['to'] == 'ryan':
        pay['email'] = config.ryan_email
      else: # get money
        pay['email'] = config.markan_email
      pay['note'] = 'sent from cucumber'
      pay['amount'] = args['amount'] if args['amount'] > 1 else 0.01 # not tryna go broke
      url = 'https://api.venmo.com/v1/payments'
      resp = requests.post(url, pay)

      if 'error' in resp.json():
        return str(resp.json()['error']['message'])
      elif 'data' in resp.json():
        return str(resp.json()['data']['payment']['status'])
      else:
        return 'wat'

    else:
      return 'invalid cucumber token'


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=7000, debug=True)
    app.run(port=7000)
