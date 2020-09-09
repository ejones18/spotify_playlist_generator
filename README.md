# spotify_playlist_recommendations
A python script that recommends a playlist based on an inputted artist and track. Now allows for playlists to be saved to your spotify account. Please see to-do list to see progress!

## What is this repository for? ##
Create a random playlist from any song you want!
* Developed and tested with Python 3.7, should work for 3.6+.

## Setup ##
* Download Python3+ from https://www.python.org/downloads/release/python-370/
* Download or clone the repository
* Install requirements using ```pip install -r requirements.txt```

# Running the *playlist_reccomendations.py script* #
* Remember to add your spotify client credientials to the constants at the top of the script from https://developer.spotify.com/dashboard/
* Navigate to the directory of the downloaded repo and run command ```python .\playlist_recommendations.py -h``` to see the CLI.
* Navigate to the directory and run the module using ```python .\playlist_recommendations.py --artist "artist name" --track "track name -s <optional_flag_to_save_playlist>"```

## Example ##
Running script for a playlist based off a track by The Killers:- \
```python .\playlist_recommendations.py --artist "Killers" --track "When The Dreams Run Dry"```

Suggested playlist:- 
``` 
Playlist: 
1) "Arabella" by Arctic Monkeys 
2) "Spaceman" by The Killers 
3) "Black Madonna" by Cage The Elephant 
4) "Everybody's Changing" by Keane
5) "Blinding Lights" by The Naked And Famous 
6) "To Death's Heart (In Three Parts)" by Bright Eyes 
7) "Simmer" by Hayley Williams 
8) "Here With Me" by The Killers 
9) "Knee Socks" by Arctic Monkeys 
10) "1901" by Phoenix 
11) "Don’t Worry" by The 1975 
12) "Agoraphobia - Acoustic" by Incubus 
13) "Maybe Tomorrow" by Stereophonics 
14) "Run For Cover" by The Killers 
15) "Imagination" by Foster The People 
16) "Mariana Trench" by Bright Eyes 
17) "Violent Sun" by Everything Everything 
18) "The Birthday Party" by The 1975 
19) "Little Secrets" by Passion Pit 
20) "Exitlude" by The Killers 
21) "Golden Touch - Full Length" by Razorlight 
22) "The Colour Of Love" by The Smashing Pumpkins
23) "Cathedrals Of The Mind" by Doves 
24) "Chelsea Dagger" by The Fratellis 
25) "Shot At The Night" by The Killers
```

## To Do ##
1. <s>Remove the need for a seed text file, allow user to search by a song and artists not seeds</s>
2. <s>Auto-fetch token if it's expired</s>
