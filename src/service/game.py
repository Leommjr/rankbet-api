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

async def get_marathonbet_games() -> List[Game]:
    marathonbetGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/marathonbet/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                marathonbetGames.append(Game(betName="marathonbet", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game["win1"], win2=game["win2"]))
            except Exception as e:
                continue

    return marathonbetGames

async def get_fonbet_games() -> List[Game]:
    fonbetGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/fonbet/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                fonbetGames.append(Game(betName="fonbet", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game['markets']["win1"]["v"], win2=game['markets']["win2"]["v"]))
            except Exception as e:
                continue

    return fonbetGames

async def get_betway_games() -> List[Game]:
    betwayGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/betway/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                betwayGames.append(Game(betName="betway", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game['markets']["win1"]["v"], win2=game['markets']["win2"]["v"]))
            except Exception as e:
                continue

    return betwayGames

async def get_ggbet_games() -> List[Game]:
    ggbetGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/ggbet/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                ggbetGames.append(Game(betName="ggbet", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game['markets']["win1"]["v"], win2=game['markets']["win2"]["v"]))
            except Exception as e:
                continue

    return ggbetGames

async def get_parimatch_games() -> List[Game]:
    parimatchGames: List[Game] = []
    async with aiohttp.ClientSession() as session:

        async with session.get('https://api.betting-api.com/parimatch/football/live/all?token=bd207bc594534134b9c38e54847eb956aeab3bc378b54411bdc5245e1272b4af') as resp:
             games = await resp.json()
        
        for game in games:
            try:
                parimatchGames.append(Game(betName="parimatch", title=game["title"], href=game["href"], team1=game['team1'], team2=game['team2'], win1=game['markets']["win1"]["v"], win2=game['markets']["win2"]["v"]))
            except Exception as e:
                continue

    return parimatchGames

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

async def get_fanduel_games() -> List[Game]:
    fanduelGames: List[Game] = []
    url = "https://odds.p.rapidapi.com/v4/sports/soccer/odds"
    querystring = {"regions":"us","oddsFormat":"decimal","markets":"h2h","dateFormat":"iso"}
    headers = {
	    "X-RapidAPI-Key": "a19972d6fdmshb445e2aac46d55ap1dd417jsnc1b125eebcd1",
	    "X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(url=url, headers=headers, params=querystring) as resp:
             games = await resp.json()
        
        for game in games:
            try:
                for entry in game['bookmakers']:
                    if(entry['key'] == "fanduel"):
                        fanduelGames.append(Game(betName="fanduel", title=game["sport_title"], href="https://sportsbook.fanduel.com/soccer", team1=entry['markets'][0]['outcomes'][0]['name'], team2=entry['markets'][0]['outcomes'][1]['name'], win1=entry['markets'][0]['outcomes'][0]['price'], win2=entry['markets'][0]['outcomes'][1]['price']))
                else:
                    continue
            except Exception as e:
                continue
    return fanduelGames