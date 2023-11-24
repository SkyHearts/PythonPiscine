from load_csv import load
# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Takes data and display the life expectancy projection of a country"""
    data = load('life_expectancy_years.csv')
    # # Display data without truncate
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    # # Check stored country name
    # country = data["country"]
    # print(country)
    # # Set header
    # header = ["country"]
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('Malaysia Life Expectancy Projections')
    # Transpose data and set to new variable
    data_T = data.set_index('country').T
    # Set axis steps
    plt.xticks(np.arange(0, 320, step=40))
    plt.yticks(np.arange(0, 100, step=10))
    # plot only Malaysia
    data_T.Malaysia.plot()
    # data_T.France.plot()
    plt.show()


if __name__ == "__main__":
    """Testing"""
    main()
