import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import random

client_id = "CLIENT ID" #remove
secret_id = "SECRET ID" #remove
redirect_uri = "REDIRECT URI"
username = "USERNAME" #remove
scope = 'user-library-read playlist-modify-public playlist-read-private playlist-modify-private' #permissions to edit playlists
playlist_id = "GOOD PLAYLIST URI" #playlist URI for my psychedelic music playlist. taken from spotify client
unwanted_id = "BAD PLAYLIST URI" #URI for a playlist of songs that i don't want in my new playlist
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=secret_id,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

def get_playlist_tracks(playlist_id): #Allows reading playlist of more than 100 songs
    results = sp.playlist_items(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

goodtracks = get_playlist_tracks(playlist_id)
badtracks = get_playlist_tracks(unwanted_id)


def gettrackdf():
    name = []
    songid = []
    artist = []
    rating = []
    for item in goodtracks:
        track = item['track']
        artist.append(track['artists'][0]['name'])
        name.append(track['name'])
        songid.append(track["id"])
        rating.append(1)
    for item in badtracks:
        track = item['track']
        artist.append(track['artists'][0]['name'])
        name.append(track['name'])
        songid.append(track["id"])
        rating.append(0)
    return pd.DataFrame({"Artist": artist, "Song Name" : name, "Song URI" : songid, "Rating": rating}) #Created a dataframe with the songs from the test set


trackdf = gettrackdf()
def get_audiofeatures(df):
    for i in range(len(df["Song URI"])): #Now need to fetch audio features. I didn't feel duration really mattered, so it's not taken
        features = sp.audio_features(df["Song URI"][i])[0]
        if features == None:
            df.drop([i])
        else:
            df.loc[i, "danceability"] = features["danceability"]
            df.loc[i, "acousticness"] = features['acousticness']
            df.loc[i, "energy"] = features['energy']
            df.loc[i, "tempo"] = features['tempo']
            df.loc[i, "instrumentalness"] = features['instrumentalness']
            df.loc[i, "loudness"] = features['loudness']
            df.loc[i, "liveness"] = features['liveness']
            df.loc[i, "key"] = features['key']
            df.loc[i, "valence"] = features['valence']
            df.loc[i, "speechiness"] = features['speechiness']
    return df


newtrackdf = get_audiofeatures(trackdf)

scaler = StandardScaler()
scaler.fit(newtrackdf.drop(["Artist", "Song Name", "Song URI", "Rating"], axis = 1))
scaled = scaler.transform(newtrackdf.drop(["Artist", "Song Name", "Song URI", "Rating"], axis = 1))
scaleddf = pd.DataFrame(scaled, columns = newtrackdf.columns[:-1])

X = scaleddf[['danceability', 'energy','tempo', 'loudness', #Some of the features are mostly the same across all songs
            'key','valence']]                                      #so I'm cutting them
y = newtrackdf["Rating"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
knn = KNeighborsClassifier(n_neighbors= 15)
knn.fit(X_train, y_train)

knn.score(X_test, y_test)

list_feat_playlists = sp.featured_playlists()


def getallfeatured_playlists(listplaylist): #takes a list of playlists and outputs a list of ids
    id = []
    for i, items in enumerate(listplaylist["playlists"]['items']):
        id.append(items['id'])
    return id


featplaylistlist = getallfeatured_playlists(list_feat_playlists)


def featplayliststracks(playlistlist): #takes a list of playlist ids and outputs a dataframe of track names and ids
    tracks = []
    for item in playlistlist:
        tracks.extend(get_playlist_tracks(item))
    name = []
    songid = []
    for item in tracks:
        track = item['track']
        name.append(track["name"])
        songid.append(track["id"])
    return pd.DataFrame({"Name": name, "Song URI": songid})


feattrackdf = featplayliststracks(featplaylistlist)

newfeattrackdf = get_audiofeatures(feattrackdf)
scaler.fit(newfeattrackdf.drop(["Name", "Song URI"], axis = 1))
scaledfeattrackdf = scaler.transform(newfeattrackdf.drop(["Name", "Song URI"], axis = 1))


##
def ratesongs(df): #I have a df of the songs i want to run through and add. I'll add things rated 1(songs i would want)to a newly generated playlist
    sp.user_playlist_create(username, "test playlist", public= False, description= "autogenerated playlist designed my me :D")
    playlist = (sp.user_playlists(username)["items"][0]["id"]) #ID of newly made playlist
    songs = [] #['danceability', 'energy','tempo', 'loudness', #Some of the features are mostly the same across all songs 'key','valence']]
    for i in range(len(df.index)):
        if knn.predict([[df.loc[0, "danceability"], df.loc[0, "energy"], df.loc[0, "tempo"], df.loc[0, "loudness"], df.loc[0, "key"], df.loc[0, "valence"]]])[0] == 1:
            songs.append(df.loc[i, "Song URI"])
    songs = random.sample(songs, 100)
    return sp.playlist_add_items(playlist, songs)

ratesongs(scaledfeatttrackdf) #ALL DONE

