import config as conf
from ramapi.client.base import BaseHTTPResourceClient


class HTTPEpisodeClient(BaseHTTPResourceClient):
    BASE_RESOURCE_URL = conf.RM_API_EPISODE_URL


class HTTPLocationClient(BaseHTTPResourceClient):
    BASE_RESOURCE_URL = conf.RM_API_LOCATION_URL


class HTTPCharacterClient(BaseHTTPResourceClient):
    BASE_RESOURCE_URL = conf.RM_API_CHARACTERS_URL
