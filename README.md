# spotify_playlist_recommendations
A python script that recommends a playlist based on an inputted artist and track. Please see to-do list to see progress!

* Update (29/05) - Track and artist search needs thorough testing as still in early access.

## What is this repository for? ##
Create a random playlist from any song you want!
* Developed and tested with Python 3.7, should work for 3.6+.

## Setup ##
* Download Python3+
* Download the repository 

## Running the app ##
* Fill in your user_id and token (Token needs replacing every hour) in the playlist_recommendations.py file, obtained from the Spotify API pages.
* Navigate to the directory of the downloaded repo and run command ```python .\playlist_recommendations.py -h``` to see the CLI.
* Run the module using ```python .\playlist_recommendations.py -a "artist name" -t "track name"```

## To Do ##
1. Remove the need for a seed text file, allow user to search by a song and artists not seeds (NEEDS THOROUGH TESTING!).
2. Convert into a flask app
3. Auth code flow to obtain refresh token
4. Save playlist to the user's spotify account
