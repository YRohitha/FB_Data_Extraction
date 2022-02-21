
# -*- coding: utf-8 -*-
"""
* Usage: 
* Programming Language: Python 3
* Author: Rohitha
"""

import urllib3
import requests
import facebook

# Define and store the app access token
token = '358277422600848|p8eUodQrk5Yvvy629lIYCv3H1qM'

# Get list of events - returns dict of all events created on Facebook having Poetry in its name
graph = facebook.GraphAPI(access_token=token, version = 13.0)
events = graph.request('/search?q=Poetry&type=event&limit=10000')

# Storing all events into a list
events_list = events['data']

# Getting the event id of the first event in the list
eventid = eventList[1][‘id’]

event1 = graph.get_object(
  id= eventid
  , fields= 
    """attending_count, can_guests_invite, category, cover, declined_count, description, end_time, guest_list_enabled, interested_count, is_canceled
    , is_page_owned, is_viewer_admin, maybe_count, noreply_count, owner, parent_group, place, ticket_uri, timezone, type, updated_time""")
attenderscount = event1[‘attending_count’]
declinerscount = event1[‘declined_count’]
interestedcount = event1[‘interested_count’]
maybecount = event1[‘maybe_count’]
noreplycount = event1[‘noreply_count’]

# Getting the list of attendees and converting list to json format
attenders = requests.get(“https://graph.facebook.com/v2.7/"+eventid+"/attending?access_token="+token+”&limit=”+str(attenderscount)) 
attenders_json = attenders.json()
                         
# Getting the admins of the event
admins = requests.get(“https://graph.facebook.com/v2.7/"+eventid+"/admins?access_token="+token)
admins_json = admins.json()
                     
# 
