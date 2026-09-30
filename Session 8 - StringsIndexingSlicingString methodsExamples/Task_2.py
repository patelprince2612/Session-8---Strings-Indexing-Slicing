# 2.
# Write a function extract_artist(song_title) that takes a string in the format 'Song Name - Artist Name' (like you see on Spotify)
# and returns just the artist's name using string slicing. Use the index() method to find the position of the dash.</em>



def extract_artist(song_title):

    artist_name_index = song_title.index("-")

    artist_name = song_title[artist_name_index+1 : ]

    print(f"artist_name {artist_name}")

song_name = input("Enter song name : ")
song_artist_name = input("Enter the artist name : ")

song_title = song_name + " - " + song_artist_name 
extract_artist(song_title)

# print(song_title)