from dataclasses import dataclass

from src.data_loader import load_json, load_map
from src.engine.validation import DataValidator


@dataclass
class GameData:
    characters: dict
    items: dict
    dialogue: dict
    announcements: dict
    quests: list
    recipes: dict
    objects: dict
    hazards: dict
    map_rows: list[str]


class DataRepository:
    def __init__(self, validator=None):
        self.validator = validator or DataValidator()

    def load(self):
        data = GameData(
            characters=load_json("characters.json"),
            items=load_json("items.json"),
            dialogue=load_json("dialogue.json"),
            announcements=load_json("announcements.json"),
            quests=load_json("quests.json"),
            recipes=load_json("recipes.json"),
            objects=load_json("objects.json"),
            hazards=load_json("hazards.json"),
            map_rows=load_map("tutorial_guild_map.txt"),
        )
        self.validator.validate_all(data.__dict__)
        return data
