"""参考 : https://qiita.com/nekocat777/items/965a85195c4c7438e2be"""

import tweepy
import json

# json読み込み
with open('./json/api_info.json', mode='r', encoding='utf_8') as j:
	keys = json.load(j)

BEARAR_TOKEN = keys["Bearar_Token"]
CONSUMER_KEY = keys["API_Key"]
CONSUMER_SECRET = keys["API_Key_Secret"]
ACCESS_TOKEN = keys["Access_Token"]
ACCESS_SECRET = keys["Access_Token_Secret"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

client = tweepy.Client(
	bearer_token = BEARAR_TOKEN,
	consumer_key = CONSUMER_KEY,
	consumer_secret = CONSUMER_SECRET,
	access_token = ACCESS_TOKEN,
	access_token_secret = ACCESS_SECRET
)

## Twitter API v2 Freeで利用できるメソッド一覧
# つぶやく
# client.create_tweet(text='json (by Twitter api free)')

#画像付きツイート
# media = api.media_upload(filename="./img/img.png")
# client.create_tweet(text="img Tweet (by Twitter api free)", media_ids=[media.media_id])