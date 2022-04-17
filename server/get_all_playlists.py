import code
from doctest import master
from platform import platform
import requests
from abc import ABC, abstractmethod
client_id = "39243b4ec71846159b2d26d29c84cae1"
client_secret = "5afc07b276be41a2be51c3f9e7bda2b1"


class Platforms ():
    @abstractmethod
    def get_access_token (self):
        pass
    @abstractmethod
    def get_playlists(self):
        pass
    @abstractmethod
    def add_music_to_playlist(self):
        pass


# class Vk_playlist (Platforms):
#     def __init__(self, user_id, token) -> None:
#         self.user_id = user_id
#         self.token = token
#     def get_playlists(self, user_id, token):
#         method = "https://api.vk.com/method/"
#         requests.post ()
#     def add_music_to_playlist(self, audio_id, owner_id, playlist_id):
#         method = "https://api.vk.com/method/audio.add"
#         data = {
#             "access_token": self.token, 
#             "v": "5.131",
#             "owner_id":  owner_id,   
#             "playlist_id": playlist_id,
#             "audio_id": audio_id
#         }
#         requests.post (method, data)

# a = Vk_playlist(8132546, token)

class Spotify_playlists_actions (Platforms):
    def get_playlists(self):
        pass
    def add_music_to_playlist(self):
        pass
    def get_access_token(self, code):
        self.response = requests.post ("https://accounts.spotify.com/api/token", data = {
                "code": code,
                "redirect_uri": "http://127.0.0.1:3000/authtoken",
                "grant_type": 'authorization_code'
            },
            headers =  {"Authorization":f"Basic {client_id}:{client_secret}"})
        print(self.response)

class Platform_factory ():
    def get_platform(self, who):
        if who == "spot":
            return  Spotify_playlists_actions ()

platform = Spotify_playlists_actions()
platform.get_access_token ("AQCKK89gvN2hXwhhPfEkp_Pq73ABZPSyMUea9H_mg75dpLm9DJ4CfaPHpa0_1f_SLo_4EyynRX-_2YlRclOp6IgPyJtlHFnk6EcVpYW7aI8AjpEkhCB-INQrnWHpDFq6EW1JSBRWhFdpTD6lzq-n-FmtErtZLuPPnDWh2ws3ql7_vzU-vauFf1JnkStV8Mpl7GRIcmrPeoCKPpkK-Oc2KdOEX83VaHv5ZwjjXNGAsFO9DhXh1CkyKeM4qYKl5xv4edClePHwpEQ41PJcycoAHGwF4rVrWmcR0nbfChye-5h_3CPghChyySFvitWoZY1FxfHO")