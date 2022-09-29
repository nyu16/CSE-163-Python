"""
Nicholas Yu
CSE163 AD
Apr 22, 2021
The python file contains a number of functions that will
utilize pandas library to get data from a data frame and be
executed as the given instructions.
"""
import pandas as pd


def species_count(data):
    """
    the function takes in a parsed pokemon data frame and
    returns the number of unique pokemon species in the dataset as
    determined by the name attribute by actively utilizing pandas
    library.
    """
    return len(data['name'].unique())


def max_level(data):
    """
    The function takes in a parsed pokemon data frame and returns a
    2-element tuple that includes the name of the pokemon and the level
    of the pokemon with the highest level in the dataset actively filtered
    by utilizing pandas library. If there is more than one pokemon with the
    highest level, then the function returns the pokemon that appears
    first in the file.
    """
    t = tuple(data.loc[data['level'].idxmax, ['name', 'level']])
    return t


def filter_range(data, low, high):
    """
    Takes in a parsed pokemon data frame and two numbers as parameters: one
    a lower bound (inclusive) and the other an upper bound (exclusive).
    The function then returns a list of the names of pokemon whose level
    fall within the bounds mentioned above in the same order that they appear
    in the dataset by actively utilizing pandas library.
    """
    range_l = list(data[(data['level'] >= low) & (data['level'] < high)].name)
    return range_l


def mean_attack_for_type(data, given_type):
    """
    This function takes a parsed pokemon data frame and a string
    representing the pokemon type as its parameters. The function
    returns the average attack value for all the pokemons in the
    dataset with the given type by actively utilizing pandas library.
    If there are no pokemons of the given type, returns None.
    """
    ave = data[data['type'] == given_type]
    ave_atk = ave['atk'].mean()
    if pd.isnull(ave_atk):
        return None
    return ave_atk


def count_types(data):
    """
    Takes a parsed pokemon data frame and returns a dictionary
    that includes the type for each pokemon and the number of
    pokemon of that type by actively grouping utilizing pandas library.
    """
    grouped = data.groupby('type')['type'].count()
    return grouped.to_dict()


def mean_attack_per_type(data):
    """
    Takes a parsed pokemon data frame and returns a dictionary
    representing average attack of pokemon of that specfic type
    by actively utilizing pandas library such as groupby function.
    """
    atk_group = data.groupby('type')['atk'].mean()
    return atk_group.to_dict()
