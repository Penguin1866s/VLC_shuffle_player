def test_random_list(randomized_list, list_songs):
    assert randomized_list != list_songs, 'The order of the elements/ songs of the random output list, is equal to de order of the original list!!!'
