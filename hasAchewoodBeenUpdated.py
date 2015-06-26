#!/usr/bin/python

import twitter
import time
import urllib2 as url
import json
from HTMLParser import HTMLParser
import achewoodTwitterCredentials
from hasAchewoodBeenUpdatedSubs import * 


no_update_message = "Still nothin'"
new_comic_message = "Damn dogg, head over to http://achewood.com/ and enjoy the new comic!"
################## MAIN ####################

todays_achewood = check_achewood()
saved_data = read_saved_data()

if (todays_achewood == ""):                                 # if nothing fetched from the web do nothing
    print "Nothing fetched"
    log("problem fetching achewood.com")
elif (saved_data == ""):                                    # if nothing is saved in the file, update the file and do nothing
    print "Nothing was saved"
    saved_data['rep'] += 1
    saved_data['last_comic'] = todays_achewood
    write_saved_data(saved_data)
    log("problem retreiving saved file")
elif (saved_data['last_comic'] == todays_achewood):         #if the comic title hasn't changed since last time - do nothing
    #no new comic - update rep and write.
    saved_data['rep'] += 1
    api = setup_tweet()
    post_tweet(api, no_update_message)
    write_saved_data(saved_data)
    log("no comic today")
else:                                                       #if there's a new title on the web, TWEET about it MAN!
    api = setup_tweet()
    post_tweet(api, new_comic_message)
    saved_data['rep'] += 1
    saved_data['last_comic'] = todays_achewood
    write_saved_data(saved_data)
    log("new comic")

