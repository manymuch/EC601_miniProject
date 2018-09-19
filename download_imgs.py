#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import wget
import warnings
import os
import argparse
import twitter_api


def setup_tweetAPI():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api

def get_media_url(tweets):
    media_files = []
    for status in tweets:
        media = status.entities.get('media', [])
        for i in range (len(media)):
            media_files.append(media[i]['media_url'])

    return media_files



def get_all_images_url(screen_name, num):
    assert type(num) is int, "numbers of pictures must be int"
    assert num > 0, "number of pictures must be postive"


    #authorize twitter, initialize tweepy
    api = setup_tweetAPI()

    tweets = api.user_timeline(screen_name=screen_name,count=10, include_rts=False,exclude_replies=True)

    assert len(tweets) is not 0, "this twitter account does not have any tweets"




    urls = get_media_url(tweets)

    #return urls here if the images in the first tweet have exceed num
    if len(urls) >= num:
        return urls[:num]

    last_id = tweets[-1].id


    #Twitter only allows access to a users most recent 3240 tweets with this method
    len_of_urls = 0
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

        if len(urls) >= num:
            return urls[:num]

    warnings.warn("Twitter only allows access to a users most recent 3240 tweets with this method. And there are only "+str(len(urls))+" images in those tweets")
    return urls


def save_imgs(media_files):


    if not os.path.exists("./images"):
        os.mkdir("./images")
    os.chdir("./images")
    i=0
    for media_file in media_files:
        i=i+1
        suffix = media_file.split(".")[-1]
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
