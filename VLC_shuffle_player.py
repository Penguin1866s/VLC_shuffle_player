from src.read_archive_xspf import read_archive_xspf
from src.obtain_songs_list import obtain_songs_list
from src.play_songs import play_songs

if __name__ == "__main__":
    path_arvhive_xspf = "list_songs.xspf"
    root = read_archive_xspf(path_arvhive_xspf)
    list_songs = obtain_songs_list(root)
    play_songs(list_songs)
