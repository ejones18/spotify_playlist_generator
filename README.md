# spotify_playlist_recommendations
A python script that recommends a playlist based on an inputted artist and track. Please see to-do list to see progress!

## What is this repository for? ##
Create a random playlist from any song you want!
* Developed and tested with Python 3.7, should work for 3.6+.

## Setup ##
* Download Python3+ from https://www.python.org/downloads/release/python-370/
* Download Node.js from https://nodejs.org/en/download/
* Download or clone the repository 

# Running the electron desktop app #
* Install all js dependencies using ```npm install```
* Spotify client credientials need adding to the engine script - see README for that script
* Start the app with ```npm start```

# Running the *playlist_reccomendations.py script* #
* Remember to add your spotify client credientials to the constants at the top of the script from https://developer.spotify.com/dashboard/
* Navigate to the directory of the downloaded repo and run command ```python .\playlist_recommendations.py -h``` to see the CLI.
* Navigate to the *engine* directory and run the module using ```python .\playlist_recommendations.py -a "artist name" -t "track name"```

## To Do ##
1. <s>Remove the need for a seed text file, allow user to search by a song and artists not seeds</s>
2. Add electron UI *underway*
3. Save playlist to the user's spotify account.
