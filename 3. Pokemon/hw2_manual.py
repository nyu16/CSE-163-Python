"""
Nicholas Yu
CSE163 AD
Apr 22, 2021
The python file contains a number of functions that will be
executed as the given instructions. Though there's a number
of functions, the functions can be divided into one that deals
with data frame and actively utilizes the pandas library, while
the other half doesn't. However, each function is a duplicate
version of another.
"""


def species_count(data):
    """
    a function species_count takes a parsed pokemon dataset and
    returns the number of unique pokemon species in the dataset as
    determined by the name attribute without using Pandas.
    """
    return len({i['name'] for i in data})


def max_level(data):
    """
    The function takes in a parsed pokemon dataset and returns a
    2-element tuple that includes the name of the pokemon and the level
    of the pokemon with the highest level in the dataset. If there is
    more than one pokemon with the highest level, then the function returns
    the pokemon that appears first in the file.
    """
    max_l = 0
    for i in data:
        if i['level'] > max_l:
            max_l = i['level']
            name = i['name']

    return (name, max_l)


def filter_range(data, low, high):
    """
    Takes in a parsed pokemon dataset and two numbers as parameters: one
    a lower bound (inclusive) and the other an upper bound (exclusive).
    The function then returns a list of the names of pokemon whose level
    fall within the bounds mentioned above in the same order that they appear
    in the dataset.
    """
    return [i['name'] for i in data if (i['level'] >= low
            and i['level'] < high)]


def mean_attack_for_type(data, poke_type):
    """
    This function takes a parsed pokemon dataset and a str representing the
    pokemon type as its parameters. The function returns the average attack
    value for all the pokemons in the dataset with the given type. If there
    are no pokemons of the given type, returns None.
    """
    count = 0
    average = 0
    for i in data:
        if i['type'] == poke_type:
            count += 1
            average += i['atk']

    if count == 0:
        return None
    return average/count


def count_types(data):
    """
    Takes a parsed pokemon dataset and returns a dictionary that includes
    the type for each pokemon and the number of pokemon of that type.
    """
    d = {}
    for i in data:
        poke_type = i['type']
        if poke_type not in d:
            d[poke_type] = 0
        d[poke_type] += 1

    return d


def mean_attack_per_type(data):
    """
    Takes a parsed pokemon dataset and returns a dictionary representing
    average attack of pokemon of that specfic type. The order of the
    keys in the returned dictionary is not in order.
    """
    poke_l = {}
    average = {}
    for i in data:
        p_type = i['type']
        if p_type not in poke_l:
            poke_l[p_type] = 0
            average[p_type] = 0
        poke_l[p_type] += i['atk']
        average[p_type] += 1

    for x in poke_l:
        poke_l[x] /= average[x]
    return poke_l
