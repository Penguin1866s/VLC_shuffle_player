import subprocess

def play_songs(randomized_list):
    songs = [song["location"] for song in randomized_list] #Comprension(its a note for me, for recording that I complete that requirement.)
    subprocess.call(["vlc", "--no-metadata-network-access"] + songs)
