from ..model.game import Game
from typing import List
import aiohttp
"""
Game services -> List all games
"""

async def get_all_games() -> List[Game]:
    allGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/1xbet/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                allGames.append(Game(betName="1xbet", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game['markets']["win1"]["v"], win2=game['markets']["win2"]["v"]))
            except Exception as e:
                continue

    return allGames

async def get_sbobet_games() -> List[Game]:
    sbobetGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/sbobet/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                sbobetGames.append(Game(betName="sbobet", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game['markets']["win1"], win2=game['markets']["win2"]))
            except Exception as e:
                continue

    return sbobetGames

async def get_pinnacle_games() -> List[Game]:
    pinnacleGames: List[Game] = []
    params = {
        "is_have_odds": "true",
        "sport_id": "1"
    }
    headers = {
        "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com",
        "x-rapidapi-key": "a19972d6fdmshb445e2aac46d55ap1dd417jsnc1b125eebcd1"
    }
    async with aiohttp.ClientSession() as session:

        async with session.get('https://pinnacle-odds.p.rapidapi.com/kit/v1/markets', headers=headers, params=params) as resp:
             games = await resp.json()
        
        for game in games["events"]:
            try:
                pinnacleGames.append(Game(betName="pinnacle", title=game["league_name"], href="https://www.pinnacle.com/pt/search/soccer/"+game["home"]+ "/participant/", team1=game['home'], team2=game['away'], win1=game['periods']['num_0']['money_line']['home'], win2=game['periods']['num_0']['money_line']['away']))
            except Exception as e:
                continue

    return pinnacleGames