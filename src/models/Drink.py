from typing import List, Dict
from pydantic import BaseModel
class Drink(BaseModel):
    name: str
    alcoholic: str
    category: str
    glass: str
    ingredients: List[Dict]
    instructions: str