from flask import Flask, request
from flask_restful import Resource, Api

from src.twint_api.request import get_tweet_from_user, get_tweet_from_search

app = Flask(__name__)
api = Api(app)

@app.route('/tweets/<string:user>', methods=['GET'])
def user_tweet(user):
    return get_tweet_from_user(user,request.args)

@app.route('/tweets/', methods=['GET'])
def search_tweet():
    return  get_tweet_from_search(request.args)


if __name__ == '__main__':
    app.run(port='5002')
