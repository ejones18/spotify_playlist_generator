# spotify_playlist_recommendations
A python script that recommends a playlist based on a randomly chosen song from a file of inputted songs. Still in very early development, see to-do list to keep track of features to be implemtented!

## What is this repository for? ##
Create a random playlist from a randomly selected song from a file of songs you like!
* Developed and tested with Python 3.7, should work for 3.6+.

## Setup ##
* Download Python3+
* Download the repository 

## Running the app ##
* Fill in your user_id and token (Token needs replacing every hour) in the playlist_recommendations.py file, obtained from the Spotify API pages.
* Populate the seed.txt with as many songs as you like using https://developer.spotify.com/console/get-search-item/
* Navigate to the directory of the downloaded repo and run command ```python .\playlist_recommendations.py -h``` to see the CLI.
* Run the module using ```python .\playlist_recommendations.py --seed-file "path/to/file/here"```

## To Do ##
1. Remove the need for a seed text file, allow user to search by a song and artists not seeds (underway).
2. Convert into a flask app
3. Auth code flow to obtain refresh token
4. Save playlist to the user's spotify account
