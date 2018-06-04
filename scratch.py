# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:08:39 2018

@author: Charles Tam
"""
from dota2api import get_api_json

LEAGUE_ID = [9643, 9601, 9862]
TEAM_ID = [1375614, 15, 543897]


def get_team_match_data(teamID,leagueID):
    team_matches_info=get_api_json('https://api.opendota.com/api/teams/{}/matches'.format(teamID))
    team_league_info=[i for i in team_matches_info for j in leagueID if i['leagueid']==j]
    team_league_match=[get_api_json('https://api.opendota.com/api/matches/{}'.format(i['match_id'])) for i in team_league_info]
    team_period_matches=[]
    for i in team_league_match:
        for j in i:
            team_period_matches=[].append(j)
    return team_league_match,team_period_matches

NB_seperate,NB_all_period=get_team_match_data(1375614,LEAGUE_ID)