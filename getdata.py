# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:13:06 2018

@author: Charles Tam
"""
from dota2api import get_api_json

LEAGUE_ID = [9643, 9601, 9862]
TEAM_ID = [1375614, 15, 543897]


def get_team_matches_data(teamid, leagueid):
    """Made for request the matches data of a team in a series of tournaments."""
    all_matches_info = get_api_json('https://api.opendota.com/api/teams/{}/matches'.format(teamid))
    leagues_matches_info = [i for i in all_matches_info for j in leagueid if i['leagueid'] == j]
    matches_details = [get_api_json\
                       ('https://api.opendota.com/api/matches/{}'.format(i['match_id']))\
                       for i in leagues_matches_info]
    return matches_details

NB_DATA = get_team_matches_data(1375614, LEAGUE_ID)
