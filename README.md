# spotify_playlist_recommendations
A python script that recommends a playlist based on an inputted artist and track. Please see to-do list to see progress!

## What is this repository for? ##
Create a random playlist from any song you want!
* Developed and tested with Python 3.7, should work for 3.6+.

## Setup ##
* Download Python3+
* Download the repository 

## Running the *playlist_reccomendations.py script* ##
* Fill in your user_id and token (Token needs replacing every hour) in the playlist_recommendations.py file, obtained from the Spotify API pages.
* Navigate to the directory of the downloaded repo and run command ```python .\playlist_recommendations.py -h``` to see the CLI.
* Run the module using ```python .\playlist_recommendations.py -a "artist name" -t "track name"```

## Running the electron desktop app ##
* Instructions to follow...

## To Do ##
1. <s>Remove the need for a seed text file, allow user to search by a song and artists not seeds</s>
2. Translaeting to JS for electron use... *underway*
3. Save playlist to the user's spotify account.
