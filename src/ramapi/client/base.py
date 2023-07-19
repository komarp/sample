import asyncio
import itertools
import typing as t
from abc import ABC

import aiohttp


class BaseHTTPResourceClient(ABC):
    BASE_RESOURCE_URL: str

    async def iter_all(self) -> t.Generator:
        num_of_pages = await self.get_num_of_pages()
        all_data = await asyncio.gather(*(self.fetch_page_data(page_num) for page_num in range(num_of_pages + 1)))
        return itertools.chain.from_iterable(all_data)

    async def get_num_of_pages(self) -> int:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_RESOURCE_URL) as response:
                data = await response.json()
            return data.get("info").get("pages")

    async def fetch_page_data(self, page_num: int) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.BASE_RESOURCE_URL}?page={page_num}") as response:
                data = await response.json()
            return data.get("results")
