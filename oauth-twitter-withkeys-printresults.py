from requests_oauthlib import OAuth1Session
# User must create their own secrets.py with the following:
# 1) client_key: Consumer Key(API Key)
# 2) client_secret: Consumer Secret (API Secret)
# 3) access_token
# 4) access_token_secret
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
r_dict = json.loads(r.text)
for entry in r_dict['statuses']:
    print('{} :'.format(entry['user']['screen_name']))
    print(entry['text'])
    print('-----------------')