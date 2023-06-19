from ..model.game import Game
from typing import List
import aiohttp

async def get_all_games() -> List[Game]:
    allGames: List[Game] = []
    url = "https://odds.p.rapidapi.com/v4/sports/soccer/odds"
    querystring = {"regions":"us,uk,eu,au","oddsFormat":"decimal","markets":"h2h","dateFormat":"iso"}
    headers = {
	"X-RapidAPI-Key": "68f38dd5acmshac010412e6c9869p111e6djsn055ac186febc",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(url=url, headers=headers, params=querystring) as resp:
             games = await resp.json()
        for game in games:
            try:
                allGames.append(Game(time=game["commence_time"].split("T")[0], id=game["id"], betName="all", title=game["sport_title"], href="na", team1=game['home_team'], team2=game['away_team'], win1=0.0, win2=0.0))
            except Exception as e:
                continue
    return allGames

async def get_all_games2() -> List[Game]:
    allGames: List[Game] = []
    url = "https://odds.p.rapidapi.com/v4/sports/soccer/odds"
    querystring = {"regions":"us,uk,eu,au","oddsFormat":"decimal","markets":"h2h","dateFormat":"iso"}
    headers = {
	"X-RapidAPI-Key": "68f38dd5acmshac010412e6c9869p111e6djsn055ac186febc",
	"X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(url=url, headers=headers, params=querystring) as resp:
             games = await resp.json()
        for game in games:
            try:
                for bookmaker in game["bookmakers"]:
                    allGames.append(Game(time=game["commence_time"].split("T")[0], id=game["id"], betName=bookmaker["key"], title=game["sport_title"], href="https://shre.ink/"+bookmaker["key"], team1=bookmaker["markets"][0]["outcomes"][0]["name"], team2=bookmaker["markets"][0]["outcomes"][1]["name"], win1=bookmaker["markets"][0]["outcomes"][0]["price"], win2=bookmaker["markets"][0]["outcomes"][1]["price"]))
            except Exception as e:
                print(e.message)
                continue
    return allGames
