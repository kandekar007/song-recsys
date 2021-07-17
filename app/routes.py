import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='x',
                                                           client_secret='x'))

from flask import render_template, json, url_for

from app.recommendations import get_recommendations, get_covers, display
from app.forms import SearchForm
from app import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():

    form = SearchForm()

    if form.validate_on_submit():

        recommendations = get_recommendations(form.search.data)
        covers = get_covers(recommendations)
        html_code = display(recommendations)


        return render_template('index.html', title = 'Song Recommendations', \
            form = form, html_code = html_code)

    return render_template('index.html', title = 'Discover similar songs', form = form)
