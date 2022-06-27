from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

# from api.elastic_test import connect_elasticsearch
# from flask_app import app
# from config.config_handling import get_config_value


es = Elasticsearch('http://localhost:9200')

app = Flask(__name__)


	
@app.route('/')
def index():
    #return render_template("index.html")
    return "This is the amazing app EVER, Abdul Rahiman Thameez"
 

@app.route('/healthz')
def healthz():
    resp = Response('ok')
    resp.headers['Custom-Header'] = 'Awesome'
    # this is awesome tying things
    return resp


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='8080')
