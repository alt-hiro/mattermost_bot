
# server.py
import message

from flask import Flask, request
import slackweb

app = Flask(__name__)

msglist = message.getAllMessage()
"""
@app.route('/')
def index():
    return 'Hello'
"""
@app.route('/', methods=['POST'])
def post():
    _returnMessage()
    print(request.headers)
    print("body: %s" % request.data)
    return request.data

def _returnMessage():
    mattermost = slackweb.Slack(url="http://52.195.12.149:8065/hooks/4q13uhsnmbntmyq7psfmk7wirr")
    mattermost.notify(text=u"私が田中だ! ちょっとおもしろいことを")
    msglist = message.getAllMessage()
    print(msglist)
    myword = message.returnMessage(msglist)
    print(myword)
    mattermost.notify(text=myword)
    mattermost.notify(text=u"なんちゃって!")

if __name__ == '__main__':
    #msglist = message.getAllMessage()
    #print(msglist)
    app.run(host='0.0.0.0', port=8080)

