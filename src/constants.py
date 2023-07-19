import datetime
from enum import Enum


class OutputFilenames(str, Enum):
    LOCATION = "locations.json"
    EPISODE = "episodes.json"
    CHARACTER = "characters.json"

    @classmethod
    def iter(cls):
        return map(lambda c: c.value, cls)


class AirDateBetween(Enum):
    START = datetime.date(2017, 1, 1)
    END = datetime.date(2021, 1, 1)


SOURCE_NAME = "RickAndMorti API"

MIN_CHARACTERS_INCLUDED_CNT = 3
