from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cucumber', methods=['GET', 'POST'])
def cucumber():
    freq = request.args['f']
    if (freq = 'yo'):
      yo()
    return freq

def yo():
    yo_all_request = requests.post("http://api.justyo.co/yoall/", data={'api_token': config.YO_API_TOKEN})
    if 'result' in yo_all_request.json() and yo_all_request.json()['result'] == 'OK':
        return json.dumps({'text': 'Yo sent to all!'})
    else:
        return json.dumps({'text': 'Error sending Yo. API may be down...'})

    return str(keys['yo_access_token'])
      

if __name__ == '__main__':
    app.run(debug=True)
