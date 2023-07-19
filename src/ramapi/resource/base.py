from abc import ABC

from ramapi.client.base import BaseHTTPResourceClient


class BaseResource(ABC):
    API_CLIENT: BaseHTTPResourceClient

    @classmethod
    async def iter_all(cls):
        return await cls.API_CLIENT.iter_all()
