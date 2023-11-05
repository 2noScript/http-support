from flask import Flask,request,jsonify
from useragent import getUserAgent
from browser_headers import getBrowserHeaders


app=Flask(__name__)


@app.route('/')
def home():
    return 'server on'

@app.route('/about')
def about():
    return jsonify({
        'version':'0.0.1',
        'author':'https://github.com/2noScript'
    })

@app.route('/generate-browser-headers',methods=['GET'])
def generateBrowserHeaders():
    limit = request.args.get('limit', default='2')
    data=getBrowserHeaders(int(limit))
    return jsonify(data)

@app.route('/generate-user-agent',methods=['GET'])
def generateUserAgent():
    limit = request.args.get('limit', default='2')
    data=getUserAgent(int(limit))
    return jsonify(data)