"""
Nicholas Yu
CSE163 AD
Apr 22, 2021
The python file imports functions from hww python files
as well as pandas library and run them through functions
that test whether hw2 functions provide expected results.
"""

import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas


def test_species_count(data, weird):
    """
    Takes in two parsed csv files, data and weird and
    tests species_count function and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(3, hw2_manual.species_count(data))
    assert_equals(5, hw2_manual.species_count(weird))


def test_max_level(data, weird):
    """
    Takes in two parsed csv files, data and weird and
    tests max_level function and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(('Lapras', 72), hw2_manual.max_level(data))
    assert_equals(('HelloWorldVillin', 100), hw2_manual.max_level(weird))


def test_filter_range(data, weird):
    """
    Takes in two parsed csv files, data and weird and
    tests filter_range function and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(data, 35, 72))
    assert_equals([],
                  hw2_manual.filter_range(data, 1, 32))
    assert_equals(['Crispee', 'Mongji', 'Pillowluv'],
                  hw2_manual.filter_range(weird, 22, 87))


def test_mean_attack_for_type(data, weird):
    """
    Takes in two parsed csv files, data and weird and
    tests mean_attack_for_type and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(47.5, hw2_manual.mean_attack_for_type(data, 'fire'))
    assert_equals(140.5, hw2_manual.mean_attack_for_type(data, 'water'))
    assert_equals(27.0, hw2_manual.mean_attack_for_type(weird, 'rubber'))


def test_count_types(data, weird):
    """
    Takes in two parsed csv files, data and weird and
    tests count_types function and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals({'fire': 2, 'water': 2}, hw2_manual.count_types(data))
    assert_equals(
        {'air': 1, 'rubber': 1, 'cat': 2, 'human': 1},
        hw2_manual.count_types(weird))


def test_mean_attack_per_type(data, weird):
    """
    Takes in two parsed csv files, data and weird and
    tests mean_attack_per_type and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(
        {'fire': 47.5, 'water': 140.5},
        hw2_manual.mean_attack_per_type(data))
    assert_equals(
        {'air': 5000.0, 'rubber': 27.0, 'cat': 10656150.5, 'human': 100.0},
        hw2_manual.mean_attack_per_type(weird))


def test_panda_species_count(data_pd, df_weird):
    """
    Takes in two dataframes, data_pd, and df_weird and
    tests pandas species_count and whether the funciton
    outputs expected value filtered through pandas. Includes
    a few other test cases apart from the given instructions.
    """
    assert_equals(3, hw2_pandas.species_count(data_pd))
    assert_equals(5, hw2_pandas.species_count(df_weird))


def test_panda_max_level(data_pd, df_weird):
    """
    Takes in two dataframes, data_pd, and df_weird and
    tests pandas max_level and whether the funciton
    outputs expected value filtered through pandas. Includes
    a few other test cases apart from the given instructions.
    """
    assert_equals(('Lapras', 72), hw2_pandas.max_level(data_pd))
    assert_equals(('HelloWorldVillin', 100), hw2_pandas.max_level(df_weird))


def test_panda_filter_range(data_pd, df_weird):
    """
    Takes in two dataframes, data_pd, and df_weird and
    tests pandas filter_range and whether the funciton
    outputs expected value filtered through pandas. Includes
    a few other test cases apart from the given instructions.
    """
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(data_pd, 35, 72))
    assert_equals(['Starmie'],
                  hw2_pandas.filter_range(data_pd, 55, 72))
    assert_equals(['Crispee', 'Mongji', 'Pillowluv'],
                  hw2_pandas.filter_range(df_weird, 22, 92))


def test_panda_mean_attack_for_type(data_pd, df_weird):
    """
    Takes in two dataframes, data_pd, and df_weird and
    tests pandas mean_attack_for_type and whether the funciton
    outputs expected value filtered through pandas. Includes
    a few other test cases apart from the given instructions.
    """
    assert_equals(47.5,
                  hw2_pandas.mean_attack_for_type(data_pd, 'fire'))
    assert_equals(140.5,
                  hw2_pandas.mean_attack_for_type(data_pd, 'water'))
    assert_equals(27.0,
                  hw2_pandas.mean_attack_for_type(df_weird, 'rubber'))


def test_panda_count_types(data_pd, df_weird):
    """
    Takes in two dataframes, data_pd, and df_weird and
    sests pandas count_types and whether the funciton
    outputs expected value filtered through pandas. Includes
    a few other test cases apart from the given instructions.
    """
    assert_equals(
        {'fire': 2, 'water': 2},
        hw2_pandas.count_types(data_pd))
    assert_equals(
        {'air': 1, 'rubber': 1, 'cat': 2, 'human': 1},
        hw2_pandas.count_types(df_weird))


def test_panda_mean_attack_per_type(data_pd, df_weird):
    """
    Takes in two dataframes, data_pd, and df_weird and
    tests pandas mean_attack_per_type and whether the funciton
    outputs expected value filtered through pandas. Includes
    a few other test cases apart from the given instructions.
    """
    assert_equals(
        {'fire': 47.5, 'water': 140.5},
        hw2_pandas.mean_attack_per_type(data_pd))
    assert_equals(
        {'air': 5000.0, 'cat': 10656150.5, 'human': 100.0, 'rubber': 27.0},
        hw2_pandas.mean_attack_per_type(df_weird))


def main():
    """
    Calls multiple test functions written above and
    run through each of them.
    """

    data = parse('/home/pokemon_test.csv')
    data_pd = pd.read_csv('/home/pokemon_test.csv')

    weird = parse('/home/weird.csv')
    df_weird = pd.read_csv('/home/weird.csv')
    # testing functions with datasets
    test_species_count(data, weird)
    test_max_level(data, weird)
    test_filter_range(data, weird)
    test_mean_attack_for_type(data, weird)
    test_count_types(data, weird)
    test_mean_attack_per_type(data, weird)
    # testing pandas functions
    test_panda_species_count(data_pd, df_weird)
    test_panda_max_level(data_pd, df_weird)
    test_panda_filter_range(data_pd, df_weird)
    test_panda_mean_attack_for_type(data_pd, df_weird)
    test_panda_count_types(data_pd, df_weird)
    test_panda_mean_attack_per_type(data_pd, df_weird)


if __name__ == '__main__':
    main()
