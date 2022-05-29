import code
from doctest import master
from logging import exception
from platform import platform
from turtle import position
from unittest import result
import requests
from abc import ABC, abstractmethod
import json
import yandex_music
# from pprint import pprint as print


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
    def get_playlists(self, access_token):
        offset_1 = 0
        self.items = ["a"]
        self.list_of_playlists = []
        while True:
            self.response = requests.get(f"https://api.spotify.com/v1/me/playlists?limit=50&offset={offset_1}", headers={
                "Authorization":'Bearer ' + access_token,
                "Content-Type": "application/json"
            })
            self.playlist_data = self.response.json ()
            offset_1 = int(self.playlist_data.get ("offset"))+int(self.playlist_data.get("limit"))
            self.items = self.playlist_data.get ("items")
            if not self.items:
                return self.list_of_playlists
            else:
                for i in self.items:
                    self.list_of_playlists.append ((i.get("name"), i.get("id"), i.get("images")))
        # print (self.user_id.get("items"))
        # self.add_track_to_playlist (self.access_token,self.list_of_playlists[4][1],self.get_only_tracks_ids(self.get_music_from_playlist (self.access_token, self.list_of_playlists[3][1])))
        
    def get_only_tracks_ids (music_data):
        lst = []
        for i in music_data:
            lst.append(i[2])
        
    def add_track_to_playlist(self,access_token,playlist_id,tracks):
        self.track_to_add_in_suitable_format = []
        for i in range (len(tracks)):
            self.track_to_add_in_suitable_format.append (f"spotify:track:{tracks[i]}")
        if (len(self.track_to_add_in_suitable_format)//100 <= 0):
            self.add_track = requests.post(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?position=0", headers={
                "Authorization":'Bearer ' + access_token,
                "Content-Type": "application/json"
                }, data=json.dumps({
                "uris":self.track_to_add_in_suitable_format,
                }))
            # print (self.add_track.text)
        else:
            for i in range (len(self.track_to_add_in_suitable_format)//100):
                self.tracks_to_add = []
                for j in range (i*100, len(self.track_to_add_in_suitable_format)-(len(self.track_to_add_in_suitable_format)//100 -1-i)*100):
                    self.tracks_to_add.append (self.track_to_add_in_suitable_format[j])
                self.add_track = requests.post(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?position=0", headers={
                "Authorization":'Bearer ' + access_token,
                "Content-Type": "application/json"
                }, data=json.dumps({
                    "uris":self.tracks_to_add,
                }))
                # print (self.add_track.text)
    
    def get_music_from_playlist (self,access_token, playlist_id):
        self.tracks = []
        offset_1 = 0
        self.items = ["a"]
        while True:
            self.music = requests.get (f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=offset,limit,items(track(name,id,artists(name)))&offset={offset_1}&limit=100', headers={"Authorization":'Bearer ' + access_token,
                "Content-Type": "application/json"})
            self.music = self.music.json()
            # print ("\n",self.music)
            offset_1 = int(self.music.get ("offset"))+int(self.music.get("limit"))
            self.items = self.music.get ("items")
            if not self.items:
                return self.tracks
            else:
                for i in self.items:
                    self.tracks.append ((i["track"]["artists"], i["track"]["name"], i["track"]["id"]))
            

    def get_access_token(self, code):
        self.response = requests.post("https://accounts.spotify.com/api/token", data={
            "code": code,
            "redirect_uri": "http://127.0.0.1:3000/authtoken",
            "grant_type": 'authorization_code',
            "client_id": client_id,
            "client_secret": client_secret,
        })
        
        self.data = self.response.json()
        try:
            self.access_token = self.data["access_token"]
        except:
            self.access_token = "error"
        self.search ("Heat Waves",['Glass Animals', 'iann dior'])
        return self.access_token
    def search (self, title: str, artists : list):
        q = ""
        for i in artists:
            q += i + " "
        print (f'{title}+{q}')
        self.response = requests.get ("https://api.spotify.com/v1/search", params= {
            'type': 'track',
            # 'include_external' : 'audio',
            "q" : f"track:{title}+artist:{q}"
        }, headers={"Authorization":'Bearer ' + self.access_token})
        print (self.response.text)
        
class Yandex_playlists_actions (Platforms):
    def get_access_token(self, code):
        pass
    def get_playlists(self,access_token):
        self.client = yandex_music.Client(access_token).init()
        self.uid = self.client["me"]["account"]["uid"]
        self.playlists_info = []
       
        self.kind = 1000
        self.empty_kinds = 0
        self.missed_playlists = 5
        while True:
            # print (self.empty_kinds)
            if self.empty_kinds >= self.missed_playlists:
                break
            try:
                self.playlist_ids =  yandex_music.playlist.playlist_id.PlaylistId(uid = self.uid, kind = self.kind, client = self.client)
                self.playlist_data = self.playlist_ids.fetch_playlist ().__dict__
            except:
                self.empty_kinds+=1
                self.kind += 1
                continue
            self.empty_kinds = 0
            self.kind += 1
            self.playlists_info.append ({"tracks":self.playlist_data['tracks'], "title":self.playlist_data['_id_attrs'][2], "playlist_uid": self.playlist_data['playlist_uuid'], "cover":self.playlist_data["cover"]})
        
        self.kind += 1
        
        self.get_tracks (self.playlists_info[0]["tracks"])
    def get_tracks (self, tracks_dict):
        self.tracks_info = []
        for i in tracks_dict:
            self.artists = []
            for j in range (len (i["track"]["artists"])):
                self.artists.append (i["track"]["artists"][j]["name"])
            
            self.tracks_info.append ({"track_id":i["id"], "title":i["track"]["title"], "artists":self.artists})
        print (self.tracks_info)
        self.search (artists= self.tracks_info[3]["artists"], title=self.tracks_info[3]["title"])
    def search (self, artists : list, title: str):
        query = title
        for i in artists:
            query += " " + i
        track_info = {"track_id": int, "title":str ,"artists": []}
        search_result = self.client.search(query).best
        track_info["track_id"] = search_result["result"]["id"]
        track_info["title"] = search_result["result"]["title"]
        for i in search_result["result"]["artists"]:
            track_info["artists"].append (i["name"])
        return track_info

        




class Platform_factory ():
    def get_platform():
        return Spotify_playlists_actions()


k = Yandex_playlists_actions()
f = Spotify_playlists_actions ()
# k.get_playlists ('AQAAAABhN2XBAAG8Xh477qOv40qEj9JVd1NIzUY')

# f.search ("Heat Waves",['Glass Animals', 'iann dior'])