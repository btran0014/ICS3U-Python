import json
import requests
artist = input("What is the artist name?:")
title = input("What is the title of the song?:")
url = 'https://api.lyrics.ovh/v1/' + artist + '/' + title

#fetching the lyrics
response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']

print(lyrics)