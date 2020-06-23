'''
    This code was based on these repositories,
    so special thanks to:
        https://github.com/datademofun/spotify-flask
        https://github.com/drshrey/spotify-flask-auth-example
        https://github.com/mari-linhares

'''

from flask import Flask, request, redirect, g, render_template, session
import spotify_wrapper

app = Flask(__name__)
app.secret_key = 'some key for session'


@app.route("/auth")
def auth():
    return redirect(spotify.AUTH_URL)

@app.route("/callback/")
def callback():
    auth_token = request.args['code']
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header
    return profile()

def valid_token(resp):
    return resp is not None and not 'error' in resp

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    if 'auth_header' in session:
        auth_header = session['auth_header']
        profile_data = spotify_wrapper.get_users_profile(auth_header)
        playlist_data = spotify_wrapper.get_users_playlists(auth_header)
        recently_played = spotify_wrapper.get_users_recently_played(auth_header)
        if valid_token(recently_played):
            return render_template("profile.html",
                               user=profile_data,
                               playlists=playlist_data["items"],
                               recently_played=recently_played["items"])
    return render_template('profile.html')

@app.route('/playlist_gen')
def playlist_gen():
    return render_template('playlist_gen.html')

if __name__ == "__main__":
    app.run(debug=True, port=spotify_wrapper.PORT)
