#!/usr/bin/python
from hasAchewoodBeenUpdatedSubs import setup_tweet

api = setup_tweet()

friends = api.GetFriends()
followers = api.GetFollowers()

for follower in followers:
   try:
      index = friends.index(follower)
      print "friend!", follower.GetName()
      
   except ValueError:
      print "not a friend following:", follower.GetName()
      try:
         api.CreateFriendship(follower.GetId())
      except:
         print "failed to create friendship :_("

      


 
