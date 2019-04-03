import urllib2
import urllib
import json
import os
from flask import render_template, Flask,jsonify,make_response, Response
from datetime import datetime
os.environ['no_proxy']='*'

app = Flask(__name__)


def wpjson():
    r = urllib2.urlopen('http://192.168.10.1/test.json')
    data=json.load(r)
    return data

@app.route('/')
def index():
    data = wpjson()
    print data['datum']
    skar = data ['data']
    deti = data ['deti']
    auta = data ['cars']
    prvni = int(skar[0])*10
    druhy = int(skar[1]) * 10
    treti = int(skar[2]) * 10
    data['nasobeni']=prvni,druhy,treti

    datum = float(data['datum'])
    data['datum']=datetime.fromtimestamp(datum).strftime('%Y-%m-%d %H:%M:%S')


    ford = auta[0]
    ford_models=ford['models']
    ford_nazev=ford['name']

    bmw = auta[1]
    bmw_models=bmw['models']
    bmw_nazev=bmw['name']

    fiat = auta[2]
    fiat_models=fiat['models']
    fiat_nazev=fiat['name']

    return render_template('index.html',data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
app.run(host='0.0.0.0',port = port)