from twython import Twython

# Replace the following strings with your own keys and secrets
TOKEN = '474185377-n28Q0EN8LQJ1FpEqcyXT8W7SWCv5eyl7DN6vs1VQ'
TOKEN_SECRET = 'vw5vj6g1DxFEn3mvIBpiuFOfD3n7aepkR1X5tT2lljeUD'
CONSUMER_KEY = '9OatfUoRO4LpjQBN6du9xXIux'
CONSUMER_SECRET = 'jeb0amO87oyDKOTw5z5dMlOA4vDpdYlm2POgj7eWe7GgO2cvPv'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="@realDonaldTrump -filter:retweets", count=5000, result_type = 'trending')


for status in data['statuses']:
    # if 'RT @realDonaldTrump' not in status['text']:
    print(status['text'])