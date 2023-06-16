from fastapi import FastAPI
from .fastapi_cache import FastAPICache
from .fastapi_cache.backends.inmemory import InMemoryBackend
from .fastapi_cache.decorator import cache
from typing import List
from .model.game import Game
from .service import game

app = FastAPI()


allGames: List[Game] = []
sbobetGames: List[Game] = []
pinnacleGames: List[Game] = []




@app.get("/live")
@app.get("/1xbet")
@cache(namespace="live", expire=10)
async def live():
    global allGames
    """Get all live games"""
    result = await game.get_all_games()
    allGames = result
    if(len(result) == 0):
        if(len(allGames) == 0):
            return {"games": []}
        else:
            return {"games": allGames}
    return {"games": result}



@app.get("/sbobet")
@cache(namespace="sbobet", expire=10)
async def sbobet():
    global sbobetGames
    """Get all sbobet games"""
    result = await game.get_sbobet_games()
    sbobetGames = result
    if(len(result) == 0):
        if(len(sbobetGames) == 0):
            return {"games": []}
        else:
            return {"games": sbobetGames}
    return {"games": result}

@app.get("/pinnacle")
@cache(namespace="pinnacle", expire=1800)
async def pinnacle():
    global pinnacleGames
    """Get all pinnacle games"""
    result = await game.get_pinnacle_games()
    pinnacleGames = result
    if(len(result) == 0):
        if(len(pinnacleGames) == 0):
            return {"games": []}
        else:
            return {"games": pinnacleGames}
    return {"games": result}


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())