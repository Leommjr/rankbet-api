from pydantic import BaseModel
from typing import List

class Match(BaseModel):
    score1: int
    score2: int

class H2h(BaseModel):
    team1: str
    team2: str
    win1: int
    win2: int
    draw: int
    matches: List[Match]