import random

def randomizer_list(list_songs):
    temp_list = list_songs[:]
    randomized_list = []
    while len(temp_list) > 0:
        random_number_to_pop = random.randint(0 , (len(temp_list) -1))
        element_list = temp_list.pop(random_number_to_pop)
        randomized_list.append(element_list)
    return randomized_list
