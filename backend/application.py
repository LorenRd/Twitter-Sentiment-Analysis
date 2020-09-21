from flask import Flask, request, jsonify
from flask_cors import CORS

import re
import pickle
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

import tweepy
from credenciales import *


app = Flask(__name__)
cors = CORS(app)

tokenizer = Tokenizer()
with open('model/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = tf.keras.models.load_model('model/model.h5')

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



@app.route('/')
def hello_world():
    return "<h1>NLP Twitter Sentiment Analysis</h1>"

@app.route('/hashtags', methods=["GET"])
def hashtags():
    data = {}
    #Hashtags from New York - 2459115 , Los Angeles - 2442047 , London - 44418
    limitHashtags = 0
    hashtags = api.trends_place(2459115)
    for ht in hashtags[0]['trends']:
        limitTweets = 0
        name = ht['name']
        tweets = {}
        for tweet in tweepy.Cursor(api.search, q=name, lang="en").items():
            if not tweet.retweeted and not tweet.text.startswith('RT'):
                tweets[limitTweets] = predictTweet(tweet.text)
                tweets[limitTweets].update({"user":tweet.user.name, "profileImage": tweet.user.profile_image_url_https})
                limitTweets = limitTweets + 1
                if limitTweets == 3:
                    break
        data[name] = tweets
        limitHashtags = limitHashtags + 1
        if limitHashtags == 3:
            break
    return jsonify(data)

@app.route('/hashtag', methods=["POST"])
def hashtag():
    data = {}
    params = request.json
    if (params != None):
        hashtag = params['hashtag']
        i = 0
        for tweet in tweepy.Cursor(api.search, q='#'+hashtag, lang="en").items():
            if not tweet.retweeted and not tweet.text.startswith('RT'):
                data[i] = predictTweet(tweet.text)
                data[i].update({"user": tweet.user.name, "profileImage": tweet.user.profile_image_url_https})
                i = i + 1
                if i == 10:
                    break
    return jsonify(data)

@app.route('/account', methods=["POST"])
def account():
    data = {}
    tweets = {}
    params = request.json
    if (params != None):
        userAccount = params['userAccount']
        try:
            i = 0
            for tweet in api.user_timeline(screen_name=userAccount, lang="en"):
                profile_info = {"user": str(tweet.user.name), "profileImage": str(tweet.user.profile_image_url_https)}
                if not tweet.retweeted and not tweet.text.startswith('RT'):
                    tweets[i] = predictTweet(tweet.text)
                    i = i + 1
                    if i == 9:
                        break
            data["profileInfo"] = profile_info
            data["tweets"] = tweets
        except tweepy.TweepError:
            print("Failed to run the command on that user, Skipping...")
    return jsonify(data)

@app.route('/predict', methods=["POST"])
def predict():
    data = {}
    params = request.json

    if (params != None):
        # Tokenize
        x_test = pad_sequences(tokenizer.texts_to_sequences([params['stringCleaned']]), maxlen=300)
        # Predict
        score = model.predict(x_test)[0]
        # Decode sentiment
        label = decode_sentiment(score)
        #response
        data["label"] = label
        data["score"] = str(score[0])

    # return a response in json format
    return jsonify(data)

def predictTweet(text):
    analysis = {}
    cleanString = preprocess(text)
    x_test = pad_sequences(tokenizer.texts_to_sequences([cleanString]), maxlen=300)
    # Predict
    score = model.predict(x_test)[0]
    # Decode sentiment
    label = decode_sentiment(score)
    # response
    analysis["text"] = text
    analysis["label"] = label
    analysis["score"] = str(score[0])
    return analysis

def preprocess(text):
    stop_words = []
    stop_words_file = open("app/model/stopwords.txt", "r")
    try:
        content = stop_words_file.read()
        stop_words = content.split(",")
    finally:
        stop_words_file.close()
    TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
    # Remove link,user and special characters
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stop_words:
            tokens.append(token)
    return " ".join(tokens)

def decode_sentiment(score, include_neutral=True):
    # SENTIMENT
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    SENTIMENT_THRESHOLDS = (0.4, 0.7)

    if include_neutral:
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

if __name__ == '__main__':
    app.run()
