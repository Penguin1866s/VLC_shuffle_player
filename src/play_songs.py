import subprocess

def play_songs(list_songs):
    songs = [song["location"] for song in list_songs] #Comprension(it's a note for me, for recording that I complete that requirement.)
    subprocess.call(["vlc", "--no-metadata-network-access"] + songs)
