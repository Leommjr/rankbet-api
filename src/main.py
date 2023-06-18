from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from .fastapi_cache import FastAPICache
from .fastapi_cache.backends.inmemory import InMemoryBackend
from .fastapi_cache.decorator import cache
from typing import List
from .model.game import Game
from .model.h2h import H2h
from .service import game, game2, premium

app = FastAPI()


allGames: List[Game] = []
allGames2: List[Game] = []
sbobetGames: List[Game] = []
pinnacleGames: List[Game] = []
parimatchGames: List[Game] = []
ggbetGames: List[Game] = []
betwayGames: List[Game] = []
fonbetGames: List[Game] = []
marathonbetGames: List[Game] = []
fanduelGames: List[Game] = []

@app.get("/live")
@app.get("/1xbet")
@cache(namespace="live", expire=10)
async def live():
    global allGames
    """Get all live games"""
    result = await game2.get_all_games()
    allGames = result
    if(len(result) == 0):
        if(len(allGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(allGames)
    return jsonable_encoder(result)

@app.get("/live2")
@cache(namespace="live", expire=10)
async def live():
    global allGames2
    """Get all live games"""
    result = await game2.get_all_games2()
    allGames2 = result
    if(len(result) == 0):
        if(len(allGames2) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(allGames2)
    return jsonable_encoder(result)

@app.get("/fanduel")
async def fanduel():
    global fanduelGames
    """Get all fanduel games"""
    result = await game2.get_fanduel_games()
    fanduelGames = result
    if(len(result) == 0):
        if(len(fanduelGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(fanduelGames)
    return jsonable_encoder(result)

@app.get("/marathonbet")
@cache(namespace="marathonbet", expire=10)
async def marathonbet():
    global marathonbetGames
    """Get all marathonbet games"""
    result = await game.get_marathonbet_games()
    marathonbetGames = result
    if(len(result) == 0):
        if(len(marathonbetGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(marathonbetGames)
    return jsonable_encoder(result)

@app.get("/fonbet")
@cache(namespace="fonbet", expire=10)
async def fonbet():
    global fonbetGames
    """Get all fonbet games"""
    result = await game.get_fonbet_games()
    fonbetGames = result
    if(len(result) == 0):
        if(len(fonbetGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(fonbetGames)
    return jsonable_encoder(result)

@app.get("/betway")
@cache(namespace="betway", expire=10)
async def betway():
    global betwayGames
    """Get all betway games"""
    result = await game.get_betway_games()
    betwayGames = result
    if(len(result) == 0):
        if(len(betwayGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(betwayGames)
    return jsonable_encoder(result)

@app.get("/ggbet")
@cache(namespace="ggbet", expire=10)
async def ggbet():
    global ggbetGames
    """Get all ggbet games"""
    result = await game.get_ggbet_games()
    ggbetGames = result
    if(len(result) == 0):
        if(len(ggbetGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(ggbetGames)
    return jsonable_encoder(result)

@app.get("/parimatch")
@cache(namespace="parimatch", expire=10)
async def parimatch():
    global parimatchGames
    """Get all parimatch games"""
    result = await game.get_parimatch_games()
    parimatchGames = result
    if(len(result) == 0):
        if(len(parimatchGames) == 0):
            return jsonable_encoder([])
        else:
            return jsonable_encoder(parimatchGames)
    return jsonable_encoder(result)


@app.get("/sbobet")
@cache(namespace="sbobet", expire=10)
async def sbobet():
    global sbobetGames
    """Get all sbobet games"""
    result = await game.get_sbobet_games()
    sbobetGames = result
    if(len(result) == 0):
        if(len(sbobetGames) == 0):
            return jsonable_encoder([])
        else:
            jsonable_encoder(sbobetGames)
    return jsonable_encoder(result)

@app.get("/pinnacle")
@cache(namespace="pinnacle", expire=1800)
async def pinnacle():
    global pinnacleGames
    """Get all pinnacle games"""
    result = await game.get_pinnacle_games()
    pinnacleGames = result
    if(len(result) == 0):
        if(len(pinnacleGames) == 0):
            return jsonable_encoder([])
        else:
            return  jsonable_encoder(pinnacleGames)
    return jsonable_encoder(result)

@app.get("/premium1")
@cache(namespace="premium1", expire=1800)
async def premium1(time: str, team1: str) -> H2h:
    """Get all premium1 games"""
    result = await premium.get_premium1_features(time, team1)
    if(result == None):
        return jsonable_encoder([])
    return jsonable_encoder(result)

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())