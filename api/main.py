from flask import Flask,request,jsonify
from fake_headers import Headers
from fake_useragent  import UserAgent

def getBrowserHeaders(limit):
    headersList=[]
    header = Headers(
        # generate any browser & os headeers
        headers=False  # don`t generate misc headers
    )
    for i in range(limit):
        headersList.append(header.generate())
    return headersList

def getUserAgent(limit):
    userList=[]
    ua = UserAgent()

    for i in range(limit):
        userList.append(ua.random)
    return userList





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