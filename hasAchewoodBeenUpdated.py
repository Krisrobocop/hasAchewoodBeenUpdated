#!/usr/bin/python

import twitter
import time
import urllib2 as url
import json
from HTMLParser import HTMLParser
import achewoodTwitterCredentials


filelocation = "/home/kris/lastachewood.txt"


no_update_message = "Still nothin'"
new_comic_message = "Damn dogg, head over to http://achewood.com/ and enjoy the new comic!"
###################function declerations.##############
def check_achewood():
    response = url.urlopen('http://www.achewood.com/')
    html = response.read()
    
    #define the HTML parser
    class MyHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self._date_of_comic = ""
        
        def handle_data(self, data):
#            if hasattr(self, '_date_of_comic'):     # checks if the instance has this attribute, if not it will create it. overriding __init__ does not work for this.  
#                print "it's in attr"
#            else:
#                print "it's not in attr"
            
            tag = self.lasttag
            if tag == "title":
                self._date_of_comic += data

            
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed(html)
#    print date_of_comic
    date_of_comic = parser._date_of_comic
    return date_of_comic;


def read_saved_data():
    myfile = open(filelocation, 'r')
    achewood_data = json.load(myfile)
    myfile.close()
    return achewood_data

def write_saved_data(data):
    myfile = open(filelocation, 'w')
    json.dump(data, myfile, indent=4)
    myfile.close()
    return

def post_tweet(message):
    api = twitter.Api(consumer_key=achewoodTwitterCredentials.twitter_consumer_key,
            consumer_secret=achewoodTwitterCredentials.twitter_consumer_secret,
            access_token_key=achewoodTwitterCredentials.the_key_given,
            access_token_secret=achewoodTwitterCredentials.the_key_secret)
    status = api.PostUpdate(message)

def log(message):
    print time.asctime(), "\t", message

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
    post_tweet(no_update_message)
    write_saved_data(saved_data)
    log("no comic today")
else:                                                       #if there's a new title on the web, TWEET about it MAN!
    post_tweet(new_comic_message)
    saved_data['rep'] += 1
    saved_data['last_comic'] = todays_achewood
    write_saved_data(saved_data)
    log("new comic")

