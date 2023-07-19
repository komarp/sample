import asyncio
import datetime
import json
import os

import aiofiles
import uvloop

import config as conf
import constants as const
from ramapi.resource.impl import Character, Episode, Location
from storage import FileStorage


class Inspector:
    def __init__(self, date_format: str = "%B %d, %Y"):
        self.date_format = date_format

    async def get_relevant_series_names(self) -> list[str]:
        result = []

        async with aiofiles.open(os.path.join(conf.OUTPUT_DIR, const.OutputFilenames.EPISODE), mode="r") as f:
            content = await f.read()
        episodes = json.loads(content)["raw_data"]

        for episode in episodes:
            if self._is_in_range(episode.get("air_date")) and len(episode["characters"]) > const.MIN_CHARACTERS_INCLUDED_CNT:
                result.append(episode["name"])

        return result

    async def get_relevant_locations(self) -> set[str]:
        blacklisted_locations = {}
        result = set()

        async with aiofiles.open(os.path.join(conf.OUTPUT_DIR, const.OutputFilenames.CHARACTER), mode="r") as f:
            content = await f.read()
        characters = json.loads(content)["raw_data"]

        for character in sorted(characters, reverse=True, key=lambda character: len(character["episode"])):
            if not blacklisted_locations.get(character["location"]["name"]):
                if self._is_only_odd_episodes(character.get("episode")):
                    result.add(character["location"]["name"])
                else:
                    blacklisted_locations[character["location"]["name"]] = 1

        return result

    @staticmethod
    def _is_only_odd_episodes(episodes: list[str]) -> bool:
        return not list(filter(lambda episode_num: episode_num % 2 == 0, [int(episode_url.split("/")[-1]) for episode_url in episodes]))

    def _is_in_range(self, air_date: str) -> bool:
        return (
            const.AirDateBetween.START.value
            <= datetime.datetime.strptime(air_date, self.date_format).date()
            <= const.AirDateBetween.END.value
        )


async def main(storage=FileStorage(), inspector=Inspector()):
    res = await asyncio.gather(*(kls.iter_all() for kls in (Location, Episode, Character)))

    await asyncio.gather(
        *(storage.store(resource_iterable, to=filename) for resource_iterable, filename in zip(res, const.OutputFilenames.iter()))
    )

    names = await inspector.get_relevant_series_names()
    locations = await inspector.get_relevant_locations()

    print(names)
    print(locations)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
