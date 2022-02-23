
# -*- coding: utf-8 -*-
"""
* Usage: 
* Programming Language: Python 3
* Author: Rohitha
Note: Generate a token and input active one to variable token.
"""

import urllib3
import requests
import facebook

# Define and store the app access token
token = '358277422600848|p8eUodQrk5Yvvy629lIYCv3H1qM'

# 
graph = facebook.GraphAPI(access_token=token, version = 13.0)
events = graph.request('/me?fields= id, name, likes')
