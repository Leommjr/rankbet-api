"""
    Game model to extract data from the APIs
"""
from pydantic import BaseModel


class Game(BaseModel):
    title: str
    team1: str
    team2: str
    win1: float
    win2: float
    href: str