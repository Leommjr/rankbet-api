from ..model.game import Game
from ..model.h2h import H2h, Match
from typing import List
import aiohttp


async def get_premium1_features(time: str, team1: str) -> H2h:
    url = "https://soccerway-feed.p.rapidapi.com/v1/matches/list"

    querystring = {"date":time}

    headers = {
	    "X-RapidAPI-Key": "68f38dd5acmshac010412e6c9869p111e6djsn055ac186febc",
	    "X-RapidAPI-Host": "soccerway-feed.p.rapidapi.com"
    }
    async with aiohttp.ClientSession() as session:

        async with session.get(url=url, headers=headers, params=querystring) as resp:
            games = await resp.json()

        for game in games["data"]:
            for matches in game["competitions"][0]["matches"]:
                if(matches["team_A"]["name"] == team1 or matches["team_B"]["name"] == team1):
                    return await get_h2h(matches["uuid"], matches["team_A"]["name"], matches["team_B"]["name"])
                

async def get_h2h(match_uuid: str, team1: str, team2: str) -> H2h:
    match_list: List[Match] = []
    url = "https://soccerway-feed.p.rapidapi.com/v1/matches/data"

    querystring = {"match_uuid": match_uuid}

    headers = {
	    "X-RapidAPI-Key": "68f38dd5acmshac010412e6c9869p111e6djsn055ac186febc",
	    "X-RapidAPI-Host": "soccerway-feed.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(url=url, headers=headers, params=querystring) as resp:
            match_data = await resp.json()
            for matches in match_data["data"]["h2h"]["matches"]:
                if(matches["team_A"]["name"] == team1):
                    match_list.append(Match(score1=matches["fts_A"], score2=matches["fts_B"]))
                else:
                    match_list.append(Match(score1=matches["fts_B"], score2=matches["fts_A"]))
            return H2h(team1=team1, team2=team2, win1=match_data["data"]["h2h"]["team_A"]["win"], win2=match_data["data"]["h2h"]["team_B"]["win"], draw=match_data["data"]["h2h"]["draw"], goals1=match_data["data"]["h2h"]["team_A"]["goal_pro"], goals2=match_data["data"]["h2h"]["team_B"]["goal_pro"], matches=match_list)

                    
            
