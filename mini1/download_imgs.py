#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import wget
import warnings
import os
import argparse


#twitter_api.py should contain your own auttentications
#must include consumer_key, consumer_secret, access_key, access_secret
from twitter_api import consumer_key as consumer_key
from twitter_api import consumer_secret as consumer_secret
from twitter_api import access_key as access_key
from twitter_api import access_secret as access_secret

def setup_tweetAPI():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api


#get all media urls from a specific tweet
def get_media_url(tweets):
    media_files = []
    for status in tweets:
        media = status.entities.get('media', [])
        for i in range (len(media)):
            media_files.append(media[i]['media_url'])

    return media_files



def get_all_images_url(screen_name, num):
    #screen_name=twitter account, num=the number of images to be downloaded
    assert type(num) is int, "numbers of pictures must be int"
    assert num > 0, "number of pictures must be postive"


    #authorize twitter, initialize tweepy
    api = setup_tweetAPI()

    try:
        tweets = api.user_timeline(screen_name=screen_name,count=10, include_rts=False,exclude_replies=True)
    except:
        print("this tweet account not available")
        exit()

    assert len(tweets) is not 0, "this twitter account does not have any tweets"



    #get all media url from the first tweet
    urls = get_media_url(tweets)

    #return urls here if the images in the first tweet have exceed num
    if len(urls) >= num:
        return urls[:num]

    last_id = tweets[-1].id


    #Twitter only allows access to a users most recent 3240 tweets with this method
    len_of_urls = 0
    #each time here try to fetch all the images from next 10 tweets of a person
    for i in range(324-1):
        more_tweets = api.user_timeline(screen_name=screen_name,
                                    count=10,
                                    include_rts=False,
                                    exclude_replies=True,
                                    max_id=last_id-1)
        assert len(more_tweets) is not 0, "no more tweets from this account"
        last_id = more_tweets[-1].id-1
        more_urls = get_media_url(more_tweets)
        urls = urls + more_urls


        if len(urls) > len_of_urls:
            len_of_urls = len(urls)
            print("got "+str(len_of_urls)+" images urls")

        #if the images here so far have exceed the requirement:num
        #the task has been done, return
        if len(urls) >= num:
            return urls[:num]

    #if 3240 tweets have been checked but the images we get here is not enough, raise warnings
    #but still return all the images from these 3240 tweets
    warnings.warn("Twitter only allows access to a users most recent 3240 tweets with this method. And there are only "+str(len(urls))+" images in those tweets")
    return urls

#saving all the images to a specific directory
def save_imgs(media_files):


    if not os.path.exists("./images"):
        os.mkdir("./images")
    os.chdir("./images")
    i=0
    for media_file in media_files:
        i=i+1
        suffix = media_file.split(".")[-1]
        #renaming these images in 1.jpg,2.jpg... etc
        wget.download(media_file,out=str(i)+"."+suffix)
    os.chdir("./../")



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--num',default=10,type=int, help='the numbers of images to download')
    args = parser.parse_args()
    num = args.num
    media_files = get_all_images_url("@JeremyClarkson",num)
    print("saving "+str(len(media_files))+" images")
    save_imgs(media_files)
