#!/usr/bin/python


import hasAchewoodBeenUpdatedSubs as subs

search_string = "achewood.com"

##pull twitter data
api = subs.setup_tweet()
search = api.GetSearch(search_string)
friends = api.GetFriends()
friendids = []

#list of IDs to check against
for friend in friends:
   friendids.append(friend.GetId())

for tweet in search:
   try:
      friendids.index(tweet.GetUser().GetId())
      print "hey, ", tweet.GetUser().GetName(), " is already a pal"
   except ValueError:
     print "make friends with ", tweet.GetUser().GetName()
     api.CreateFriendship(tweet.GetUser().GetId())
