import twittertweets
CONSUMER_KEY = '	ya8O4M8jZ6R7FOFQYgGzQJjdi'
CONSUMER_SECRET = 'OjxQraLz3i9mWirbrZ2s3BexH3L2W3ReqOCZgvbasXg0XfOZQe'
OAUTH_TOKEN = '	4875870789-kNvf2XjMoFyauWCHBOZNKvbE5SKohYnOIGPI0vb'
OAUTH_TOKEN_SECRET = '	3HNS2BFVZiNd2SOfiAlMpJiL1rheM7rGclxh2VxvqCirM'

auth = twittertweets.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twittertweets.Twitter(auth=auth)
print twitter_api # Nothing to see by displaying twitter_api except that it's now a defined variable

q = '#hema' # Use this variable to search for a hashtag.
count = 100 # the number of results to retrieve

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses'] #extract the tweets found

import json
print json.dumps(statuses[0], indent=1)