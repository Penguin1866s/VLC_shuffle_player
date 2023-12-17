import random

def randomizer_list(list_songs):
    randomized_list = list_songs[:]
    random.shuffle(randomized_list)
    return randomized_list
