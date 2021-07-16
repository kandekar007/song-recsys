import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from . import spotify2, preprocessing
import pandas as pd
import pickle
# root=".\\"
# os.chdir(root)
def get_recommendations(search):
    
    #Init
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='46a6b87f2b4a45df98b3df758f0cc652', client_secret='70d6b2094c544e5eb91b45e29522f388'))

    song_name=[{'name': search}]

    # model = pickle.load(open("D:\Placements\WebDev\SongRecommender_v1.0\SongRecommender\\app\model.pkl", 'rb'))
    path1 =  os.path.abspath("./app/model.pkl")
    model = pickle.load(open(path1, 'rb'))
    scaler = model.steps[0][1]
    # spotify_data = pd.read_csv('D:\Placements\WebDev\SongRecommender_v1.0\SongRecommender\\app\data_preprocessed.csv')
    path2 =  os.path.abspath("./app/data_preprocessed.csv")
    spotify_data = pd.read_csv(path2)
    recommendations = spotify2.recommend_songs(song_name, scaler, spotify_data,n_songs=10)
    return recommendations
    
def get_covers(recommendations):
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='46a6b87f2b4a45df98b3df758f0cc652',
                                                               client_secret='70d6b2094c544e5eb91b45e29522f388'))
    result={}
    id_list=[]
    for i in range(0,len(recommendations)):
        rec=recommendations[i]['name']
        result.update(sp.search(q = rec, type = 'track', limit = 1))
        id_list.append(result['tracks']['items'][0]['id'])

    tracks = sp.tracks(id_list)
    cover_links = [image['album']['images'][2]['url'] for image in tracks['tracks']]

    return cover_links, tracks

def display(recommendations):

    html_display = ''
    covers, tracks = get_covers(recommendations)
    
    for idx, track in enumerate(tracks['tracks']):

        html_display += f'''
            <div class = 'row recommendation'>
                <div class = 'col-md-2'>
                    <img src = "{covers[idx]}">
                </div>
                <div class = 'col-md-6 info'>
        
                    <p>{track['name']} by {track['artists'][0]['name']}</p>
                </div>
                <div class = 'col-md-4'>
                    <a href = "{track['external_urls']['spotify']}" target = '_blank'><button class = 'button'>Play It</button></a>
                </div>
            </div>
        '''
    return html_display
