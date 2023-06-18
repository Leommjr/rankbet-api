"""
    Game model to extract data from the APIs
"""
from pydantic import BaseModel
from typing import Union

class Game(BaseModel):
    time: Union[str, None] = None
    id: Union[str, None] = None
    betName: str
    title: str
    team1: str
    team2: str
    win1: float
    win2: float
    href: str