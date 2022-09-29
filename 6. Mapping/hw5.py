"""
Nicholas Yu
CSE163 AD
May 13, 2021
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def load_in_data(first, second):
    """
    The function takes in two parameters which are the filename for
    the census dataset and the filename for the food access dataset.
    Then, the function merges the two datasets on CTIDFP00 and
    CensusTract, and returns the result as a GeoDataFrame. Since the
    focus is set on geo dataframe the resulting data frame is 1318x30.
    """
    df1 = gpd.read_file(first)
    df2 = pd.read_csv(second)

    merged = df1.merge(df2, left_on='CTIDFP00',
                       right_on='CensusTract', how='left')

    return merged


def percentage_food_data(data):
    """
    A function that takes in a merged data from the previous function
    and returns the percentage of census tracts in Washington for the
    food access data that is provided. The percentage is float value
    multiplied by 100
    """
    return len(data[data['State'] == 'WA'])/len(data['State']) * 100


def plot_map(data):
    """
    The function takes in the merged data and plots the shapes of all
    the census tracts in Washington, which evenetually is outputted as
    Washington state covered in blue regions, and then stored as map.png.
    The plot is titled "Washington State".
    """
    data.plot()
    plt.title('Washington State')

    plt.savefig('map.png')


def plot_population_map(data):
    """
    A function that takes in merged data as a parameter and plots the
    shapes of all the census tracts in Washington, and each census
    tract is colored accordingly to population. The plot consists of
    Washington in the background color #EEEEEE, has a legend to indicate
    the meaning of each census tract color, and is stored as a file name
    population_map.png.
    """
    fig, ax = plt.subplots(1)

    data.plot(color='#EEEEEE', ax=ax)
    data.plot(column='POP2010', ax=ax, legend='True')
    plt.title('Washington Census Tract Populations')

    plt.savefig('population_map.png')


def plot_population_county_map(df):
    """
    The function receives the merged data as a parameter and plots the
    shapes of all the census tracts in Washington. In the plot, each
    county is colored according to population. The data is previously
    'grouped by' each county, and displays the map accordingly. The plot
    includes a legend for each census tract color and is stored as
    county_population_map.png.
    """
    fig, ax = plt.subplots(1)
    data = df.loc[:, ['POP2010', 'County', 'geometry']]

    county = data.dissolve(by='County', aggfunc='sum')

    data.plot(color='#EEEEEE', ax=ax)
    county.plot(column='POP2010', ax=ax, legend='True')
    plt.title("Washington County Populations")

    plt.savefig('county_population_map.png')


def plot_food_access_by_county(state_data):
    """
    The function takes in a merged dataframe and produces 4 plots on the
    same figure plotting information about food access across income level.
    Each plot originally computed the ratio of people in each category, and
    plotted on different subplots ax1, ax2, ax3, and ax4, and each plot has
    a legend showing income levels for different counties depending on
    different criteria. The plots are later saved as county_food_access.png.
    """
    data = state_data.loc[:, ['County', 'geometry', 'POP2010', 'lapophalf',
                              'lapop10', 'lalowihalf', 'lalowi10']]
    county = data.dissolve(by='County', aggfunc='sum')

    county['lapophalf_ratio'] = county['lapophalf']/county['POP2010']
    county['lapop10_ratio'] = county['lapop10']/county['POP2010']
    county['lalowihalf_ratio'] = county['lalowihalf']/county['POP2010']
    county['lalowi10_ratio'] = county['lalowi10']/county['POP2010']

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))

    data.plot(color='#EEEEEE', ax=ax1)
    data.plot(color='#EEEEEE', ax=ax2)
    data.plot(color='#EEEEEE', ax=ax3)
    data.plot(color='#EEEEEE', ax=ax4)
    county.plot(column='lapophalf_ratio', vmin=0, vmax=1,
                legend='True', ax=ax1)
    county.plot(column='lalowihalf_ratio', vmin=0, vmax=1,
                legend='True', ax=ax2)
    county.plot(column='lapop10_ratio', vmin=0, vmax=1,
                legend='True', ax=ax3)
    county.plot(column='lalowi10_ratio', vmin=0, vmax=1,
                legend='True', ax=ax4)

    ax1.set_title('Low Access: Half')
    ax2.set_title('Low Access + Low Income: Half')
    ax3.set_title('Low Access: 10')
    ax4.set_title('Low Access + Low Income: 10')

    plt.savefig('county_food_access.png')


def plot_low_access_tracts(state_data):
    """
    The function takes in the merged data and plots all census tracts
    considered "low access". The function first computes statistics for
    each census tract depending on its classification as Urban or Rural.
    Then, the function filters data based on whether the 'Urban' (or rural)
    has low access population of over 500 people or 33% of the overall
    tract population. Then, we produce a layered plot same axes to
    highlight low access census tracts and saved as low_access.png file.
    """
    fig, ax = plt.subplots(1)
    low_data = state_data[
        (state_data['Urban'] == 1) | (state_data['Rural'] == 1)]

    urban = state_data[(state_data['Urban'] == 1)]
    rural = state_data[(state_data['Rural'] == 1)]
    urban_la = urban[(urban['lapophalf'] >= 500) |
                     (urban['lapophalf']/urban['POP2010'] >= 0.33)]
    rural_la = rural[(rural['lapop10'] >= 500) |
                     (rural['lapop10']/rural['POP2010'] >= 0.33)]

    state_data.plot(color='#EEEEEE', ax=ax)
    low_data.plot(color='#AAAAAA', ax=ax)
    urban_la.plot(ax=ax)
    rural_la.plot(ax=ax)
    plt.title("Low Access Census Tracts")

    plt.savefig('low_access.png')


def main():
    """
    main function to call above function as well as form a dataframe
    to be used throughout different functions.
    """
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
