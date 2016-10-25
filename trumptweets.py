from twython import Twython
import pickle
import os

# data = t.search(q="@realDonaldTrump -filter:retweets", count=100, result_type = 'trending')


# for status in data['statuses']:
#     # if 'RT @realDonaldTrump' not in status['text']:
#     print(status['text'])

def create_file(filename, query):
    '''
    This function creates a new pickle file containing a list of tweets
    resulting from the input query.
    Inputs: 
        filename - This is the name of the file you want to use to save the tweets in
        query - This is the twitter search query to use to search for tweets and can 
                include operators like AND, OR and NOT, and also 'filter: retweets'
    '''
    # Replace the following strings with your own keys and secrets
    TOKEN = '474185377-n28Q0EN8LQJ1FpEqcyXT8W7SWCv5eyl7DN6vs1VQ'
    TOKEN_SECRET = 'vw5vj6g1DxFEn3mvIBpiuFOfD3n7aepkR1X5tT2lljeUD'
    CONSUMER_KEY = '9OatfUoRO4LpjQBN6du9xXIux'
    CONSUMER_SECRET = 'jeb0amO87oyDKOTw5z5dMlOA4vDpdYlm2POgj7eWe7GgO2cvPv'

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

    data = t.search(q=query, count=100, result_type = 'mixed')

    filename += '.pickle'

    if not os.path.exists(filename):
        f = open(filename,'w')
        pickle.dump(data,f)
        f.close
        print('File created as %s.' % filename)
    else:
        print("File %s already exists. Use load_file(filename) to open it" % filename)


create_file('trumptweets', "@realDonaldTrump -filter:retweets")