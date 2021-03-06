# Hit the Twitter API and pull either the public timeline or a user
# timeline, and then print a selection of data.
# UTF-8 encoding is necessary especially when dealing with public
# timeline.

# Use the requests module
import twitter

api = twitter.Api(consumer_key='your-consumer-key',
                  consumer_secret='your-consumer-secret',
                  access_token_key='your-access-token-key',
                  access_token_secret='your-access-token-secret')

# set a handle
handle = 'anthonydb'

# Get some info on a user
user = api.GetUser(handle)
print user.GetName()
print user.GetFollowersCount()
print user.GetDescription()


# get a user timeline
statuses = api.GetUserTimeline('usatoday', count=1)
print [s.text for s in statuses]

# get a user timeline
#statuses = api.GetPublicTimeline()
#print [s.text for s in statuses]
