#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '9gqIhQvRcKaCnszpPIJQRomNF'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Zgf9RMpDDVeDMQaRhA5OebdaQl8TqRiQ6qhLfZ5dSFfYmryaxS'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3659277502-I1Wx27SQln9Hek71160ziRmMcsHwjcxos9JfWrH'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'skxxEnSjuVom4SNzRGhS7eX60cE4uqulUQtpslmSsC6LB'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
