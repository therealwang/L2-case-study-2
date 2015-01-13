#This code grabs relevant information on big brands from their twitter profile

import tweepy, shutil, csv, time
from tempfile import NamedTemporaryFile
import pandas as pd 

consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_secret = '***'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api=tweepy.API(auth) #authorization for twitter API

l2 = pd.read_csv('l2.csv') #reads in CSV for analysis

for i in range(0,len(l2)):
	temp = l2.iloc[i,0]
	for users in tweepy.Cursor(api.search_users,q=temp).items(1):
		temp = users #twitter search for brand account
	if temp.verified or 'official' in temp.description: #some brands aren't twitter verified but are still official (eg YSL Beauty)
		l2.iloc[i,1]='Y'
		l2.iloc[i,2]=temp.screen_name #twitter handle
		localtime = time.asctime( time.localtime(time.time()) )
		l2.iloc[i,4]=localtime #time data was obtained
		l2.iloc[i,5]=temp.followers_count #follower count
		l2.iloc[i,6]=temp.statuses_count #tweet count
	else:
		l2.iloc[i,1]='N' #if there is no official account, no data is retrieved


l2 = l2.iloc[:,[0,1,2,4,5,6]]
pd.DataFrame.to_csv(l2,'l2t.csv') #outputs a CSV file for viewing


