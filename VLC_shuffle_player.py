from src.read_archive_xspf import read_archive_xspf
from src.obtain_songs_list import obtain_songs_list
from src.randomizer_list import randomizer_list
from src.play_songs import play_songs

from test.test_random_list import test_random_list
from test.test_no_xspf import test_no_xspf

if __name__ == "__main__":
    path_arvhive_xspf = "list_songs.xspf"
    root = read_archive_xspf(path_arvhive_xspf)
    list_songs = obtain_songs_list(root)
    randomized_list = randomizer_list(list_songs)

    #tests:
    test_random_list(randomized_list, list_songs)
    test_no_xspf(path_arvhive_xspf)

    #The execution of VLC_shuffle_player:
    play_songs(randomized_list)
