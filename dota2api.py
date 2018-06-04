# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:15:55 2018

@author: Charles Tam

Powered by He Qiuzhi
"""

import requests

def get_api_json(url):
    try:
        r = requests.get(url, timeout=3)
        r_json = r.json()
        return r_json
    except:
        return get_api_json(url)

if __name__ == '__main__':
    pass