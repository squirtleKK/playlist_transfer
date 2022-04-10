from doctest import master
import requests
from abc import ABC, abstractmethod



class Platforms ():
    @abstractmethod
    def get_playlists():
        pass
    @abstractmethod
    def add_music_to_playlist():
        pass
    @abstractmethod
    def add_music ():
        pass


class Vk_playlist (Platforms):
    def __init__(self, user_id, token) -> None:
        self.user_id = user_id
        self.token = token
    def get_playlists(self, user_id, token):
        method = "https://api.vk.com/method/"
        requests.post ()
    def add_music_to_playlist(self, audio_id, owner_id, playlist_id):
        method = "https://api.vk.com/method/audio.add"
        data = {
            "access_token": self.token, 
            "v": "5.131",
            "owner_id":  owner_id,   
            "playlist_id": playlist_id,
            "audio_id": audio_id
        }
        requests.post (method, data)

a = Vk_playlist(8132546, token)
