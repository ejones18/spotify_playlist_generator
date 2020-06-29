"""
A python script that fetches song recommendations using the Spotify API
- Credit rob_med from medium.com
- Ethan Jones <ejones18@sheffield.ac.uk>
- First authored: 2020-05-25
"""
import argparse
import sys
import requests

def main(artist, track):
    """
    Print a 25 song-long playlist based on a randomly chosen input song
    """
    seeds = search_artist_track(artist, track)
    query_api(seeds)

def search_artist_track(artist, track):
    """
    Searches the Spotify API for the artist and track, returns the json response
    """
    track = track.replace(" ", "+")
    settings = define_settings()
    endpoint_url = "https://api.spotify.com/v1/search?"
    query = f'{endpoint_url}'
    query += f'q=track%3A{track}%20artist%3A{artist}&type=track'
    response = requests.get(query,
                            headers={"Content-Type":"application/json",
                                     "Authorization":f"Bearer {settings[1]}"})
    json_response = response.json()
    seeds = get_track_artist_id_from_json(json_response)
    return seeds

def get_track_artist_id_from_json(json_response):
    """
    Gets the track and artist ID from the json response from the API search
    """
    seeds = [(json_response['tracks']['items'][0]['artists'][0]['id']),
             (json_response['tracks']['items'][0]['id'])]
    return seeds

def define_settings():
    """
    Sets the endpoint as well as defines the token
    """
    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    token = "BQCSrX8OYSynb1QS65WhKHF_KM2sIrmZ33ZUI010o2tvt39CdFAYmb3_lS3CPIpt7U4mkB9wKJdiP1swGjv3aJWJ-YoPQ9aIAeI5rIpVmQzp8LK4rF-abYYhV9jQ36NJsR2DQEa0hoGxgvly7cYMbUW1slcBRGAnSDdX6VTO2C0DLnnRQF3YM3POHHDESWBGOYdRxG3JFFplqHgjeuTinzi3Trw8vBDegDfvMX0dAO1uJyvZyVg5W_69cTA8E2vGADaPgRcvzbR_vhw"
    settings = [endpoint_url, token]
    return settings

def define_filters(seeds):
    """
    Sets the filters i.e. number of songs and genre
    """
    limit = 25
    market = "GB"
    seed_genres = "indie"
    seed_artists = seeds[0]
    seed_tracks = seeds[1]
    filters = [limit, market, seed_genres, seed_artists, seed_tracks]
    return filters

def query_api(seeds):
    """
    Queries the Spotify API and returns a json response
    """
    settings = define_settings()
    filters = define_filters(seeds)
    query = f'{settings[0]}limit={filters[0]}&market={filters[1]}&seed_genres={filters[2]}'
    query += f'&seed_artists={filters[3]}'
    query += f'&seed_tracks={filters[4]}'
    response = requests.get(query,
                            headers={"Content-Type":"application/json",
                                     "Authorization":f"Bearer {settings[1]}"})
    json_response = response.json()
    print_output(json_response)

def print_output(json_response):
    """
    Prints the output
    """
    uris = []
    print('Recommended Songs:')
    for i, j in enumerate(json_response['tracks']):
        uris.append(j['uri'])
        print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")
    sys.stdout.flush()

def parse_options():
    """Parse command line options."""
    parser = argparse.ArgumentParser(description=("This is a command line interface (CLI) for "
                                                  "the playlist_reccomendation module"),
                                     epilog="Ethan Jones, 2020-05-25")
    parser.add_argument("-a", dest="artist", action="store", type=str,
                        required=True, metavar="name_of_artist",
                        help="Artist name.")
    parser.add_argument("-t", dest="track", action="store", type=str,
                        required=True, metavar="name_of_track",
                        help="Track name.")
    options = parser.parse_args()
    return options

if __name__ == "__main__":
    #OPTIONS = parse_options()
    artist = sys.argv[1]
    track = sys.argv[2]
    main(artist, track)
