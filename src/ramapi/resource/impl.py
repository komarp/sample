from ramapi.client.impl import HTTPCharacterClient, HTTPEpisodeClient, HTTPLocationClient
from ramapi.resource.base import BaseResource


class Episode(BaseResource):
    API_CLIENT = HTTPEpisodeClient()


class Location(BaseResource):
    API_CLIENT = HTTPLocationClient()


class Character(BaseResource):
    API_CLIENT = HTTPCharacterClient()
