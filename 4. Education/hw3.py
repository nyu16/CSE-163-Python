"""
Nicholas Yu
CSE163 AD
April 29, 2021
This python file is a collection of fuctions that returns DataFrames
wit filtered information, produce seaborn graphs based on data, and
applies the data machine learning process eventually. Each function
takes in DataFrame read from the main function. The whole purpose of
this python file is an practice exercise for reviewing data visualization,
data managing, and small part of machine learning.
"""

import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split


def compare_bachelors_1980(data):
    """
    The function takes in a data from the parameter and returns the result
    as a 2-by-2 DataFrame with rows displaying data of men and women, and
    columns showing data of Sex and Total. The function eventually show the
    percentages for women vs men having earned a Bachelor's degree in 1980
    """
    gender = data[(data['Sex'] == 'M') | (data['Sex'] == 'F')]
    df = gender[(gender['Year'] == 1980) &
                (gender['Min degree'] == "bachelor's")]

    return df.loc[:, ['Sex', 'Total']]


def top_2_2000s(df, sex='A'):
    """
    The function takes in a data and a Sex filter value that is set to 'A', as
    in all students, on default. Then returns a 2-element Series. The function
    compares educational attainment levels and show the 2 most commonly awarded
    levels of degress awarded between 2000 and 2010 for a given gender. The
    index of the returned Series is the Min degree and the values its mean.
    """
    data = df[(df['Year'] >= 2000) & (df['Year'] <= 2010)]
    gender = data[data['Sex'] == sex]
    s = gender.groupby('Min degree')['Total'].mean()

    return s.nlargest(2)


def line_plot_bachelors(df):
    """
    Takes in as a paramter the data, and plots a seaborn line chart of the
    total percentages of all people Sex A with bachelor's Min degree over
    time. The x-axis represent Year, the y-axis Percentage, and title is
    Percentage Earning Bachelor's over Time, then is saved as a png file.
    """
    data = df[(df['Min degree'] == "bachelor's") & (df['Sex'] == 'A')]

    sns.relplot(data=data, x="Year", y="Total", kind="line")

    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("Percentage Earning Bachelor's over Time")

    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(df):
    """
    The function takes in a data and plots a seaborn bar chart comparing
    the total percentages of Sex F, M, and A with high school Min degree
    in the Year 2009. The x-axis represents Sex, the y-axis Percentage,
    and the graph is saved as a png file.
    """
    barDf = df[(df['Min degree'] == 'high school') & (df['Year'] == 2009)]

    sns.catplot(data=barDf, y='Total', x='Sex', kind="bar")

    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.title('Percentage Completed High School by Sex')

    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(df):
    """
    The function takes in as a parameter a data, and plots how the
    percentage of Hispanic people with degrees have changed between
    1990–2010 (inclusive) for high school and bachelor's Min degree.
    Then, based on the data, seaborn plots a line graph with x-axis as
    Year, the y-axis Hispanic, and displays two distinctive lines each
    representing two different Min degree.
    """
    yrDf = df[(df['Year'] >= 1990) & (df['Year'] <= 2010)]
    data = yrDf[(yrDf['Min degree'] == 'high school') |
                (yrDf['Min degree'] == "bachelor's")]
    sns.relplot(data=data, x='Year',
                y="Hispanic", hue='Min degree', kind="line")

    plt.title("Hispanic's Degrees Percentage Change Between 1990 and 2010")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.xticks(rotation=45)

    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    The function trains a DecisionTreeRegressor to predict the total
    percentage of Sex based on Min degree, Year, and Sex.The function
    returns the test mean squared error as a float after. Filters the
    data columns to only include Year, Min degree, Sex, and Total and
    drops rows with Nan values.
    """
    df = data.loc[:, ['Year', 'Min degree', 'Sex', 'Total']]
    df = df.dropna()

    labels = df['Total']
    features = pd.get_dummies(df.loc[:, df.columns != 'Total'])

    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)

    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)

    predictions = model.predict(features_test)

    return (mean_squared_error(labels_test, predictions))


def main():
    """
    The main function reads the csv data and converts it into a
    DataFrame using pandas library. Then passes the dataframe to
    each function that it calls in it.
    """
    data = pd.read_csv('nces-ed-attainment.csv', na_values=['---'])
    sns.set()

    compare_bachelors_1980(data)
    top_2_2000s(data, 'A')
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
