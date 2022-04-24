import code
from doctest import master
from http import client
from platform import platform
import requests
from abc import ABC, abstractmethod
import json
client_id = "39243b4ec71846159b2d26d29c84cae1"
client_secret = "5afc07b276be41a2be51c3f9e7bda2b1"


class Platforms ():
    @abstractmethod
    def get_access_token(self):
        pass

    @abstractmethod
    def get_playlists(self):
        pass

    @abstractmethod
    def add_music_to_playlist(self):
        pass

    @abstractmethod
    def get_music_from_playlist (self):
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
        self.response = requests.get("https://api.spotify.com/v1/me/playlists", headers={
            "Authorization":'Bearer ' + self.access_token,
            "Content-Type": "application/json"
        })
        self.user_id = self.response.json ()
        self.list_of_playlists = []
        print (self.user_id.get("items"))
        for i in self.user_id.get("items"):
            self.list_of_playlists.append ((i.get("name"), i.get("id"), i.get("images")))
        # print ("\n", self.list_of_playlists[0][1])
        print ("\n", self.get_music_from_playlist(self.list_of_playlists[3][1]))
        
    def add_track_to_playlist(self,playlist_id,track):
        self.add_track = requests.post(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers={
            "Authorization":'Bearer ' + self.access_token,
            "Content-Type": "application/json"
        }, data={
            "uris": [f"spotify:track:{track}"]
        })
    def get_music_from_playlist (self, playlist_id):
        self.music = requests.get (f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items(track(name,id,artists(name)))', headers={"Authorization":'Bearer ' + self.access_token,
            "Content-Type": "application/json"})
        return self.music.json()
    def get_access_token(self, code):
        self.response = requests.post("https://accounts.spotify.com/api/token", data={
            "code": code,
            "redirect_uri": "http://127.0.0.1:3000/authtoken",
            "grant_type": 'authorization_code',
            "client_id": client_id,
            "client_secret": client_secret,
        })
        self.data = self.response.json()
        self.access_token = self.data["access_token"]
        print(self.access_token)


class Platform_factory ():
    def get_platform():
        return Spotify_playlists_actions()
