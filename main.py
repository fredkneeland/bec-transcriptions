import datetime

# import google
# import sys
# import json
# gae_dir = google.__path__.append('/Users/fredkneeland/google-cloud-sdk/platform/google_appengine/google')
# sys.path.insert(0, gae_dir) # might not be necessary

# from google.cloud import ndb
from flask import Flask, jsonify, request, render_template
# from lib.bottle import get, post, request, response

# import models


app = Flask(__name__)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)

texts = [""]

@app.route('/updatetext/', methods=['POST'])
def update_text():
    text = request.get_json()
    texts[0] = text.get('texts')
    return jsonify(texts)

@app.route('/mytext/', methods=['GET'])
def my_text():
	return jsonify(texts)

# Not sure if these should go here or not?
# @post('/login')
# def login():
# 	print("login")
#     # userID = request.json.get('userID')
#     # userInfo = models.User.query().filter(models.User.userID == userID).fetch(1)
#     # return models.login_to_json(userInfo[0])


# # eventually I want to add an id to associate this text with its particular audio file
# @post('/updateText')
# def updateText():
# 	print("updateText")
# 	return json.dumps(["hello world"])
#     # user = users.get_current_user()
#     # userID = user.user_id()
#     # userInfo = models.User.query().filter(models.User.userID == userID).fetch(1)
    
#     # if userInfo is None or len(userInfo) == 0:
#     #     logging.info("updateText")
#     #     logging.info(request.json.get('texts'))
#     #     user = models.User(userID=userID, texts=request.json.get('texts'))
#     #     user.put()
#     # else:
#     #     userInfo[0].days = request.json.get('texts')
#     #     userInfo[0].put()
#     # return json.dumps([])

# @get('/mytext/')
# def get_my_text():
# 	print("get my text")
# 	return json.dumps("hello world")
#     # user = users.get_current_user()
#     # userID = user.user_id()
#     # userInfo = models.User.query().filter(models.User.userID == userID).fetch(1)

#     # response.content_type = 'application/json'
#     # to_return = [""]

#     # if userInfo is None or len(userInfo) == 0:
#     #     logging.info("mytext")
#     #     logging.info(to_return)
#     #     return json.dumps(to_return)

#     # if len(userInfo[0].texts) > 0:
#     #     to_return[0] = append(userInfo[0].texts)

#     # to_return
#     # return json.dumps(to_return)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)