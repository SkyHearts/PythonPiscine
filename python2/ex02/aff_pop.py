from load_csv import load
import matplotlib.pyplot as plt
# import matplotlib.colors as col
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd


def clSuf(x):
    """Clean suffix such as B, M and k"""
    if isinstance(x, str):
        return (x.replace('B', 'e9').replace('M', 'e6').replace('k', 'e3'))
    return x


def dropYear(data: pd.DataFrame, start: int, end: int):
    """Drops years outside of set range"""
    for dataCol in data.columns:
        if dataCol == "country":
            continue
        if int(dataCol) in range(start, end + 1):
            continue
        else:
            data.drop(dataCol, axis='columns', inplace=True)


def format(x, pos):
    """Converts the char k, M, B to their respective value"""
    if (x >= 1000000000):
        return '%1.1fB' % (x*1e-9)
    if (x >= 1000000):
        return '%1.0fM' % (x*1e-6)
    if (x >= 1000):
        return '%1.0fk' % (x*1e-3)


def main():
    try:
        """Plot  population projection of malaysia and another country"""
        data = load('population_total.csv')
        assert data is not None, "File Does Not Exist/wrong type"
        # Drop year outside a certain range
        dropYear(data, 1800, 2050)
        # Transpose data and set to new variable
        data_T = data.set_index('country').T
        # apply the function clSuf to specific column and covert to float
        data_T["France"] = data_T["France"].apply(clSuf).astype('float')
        data_T["Malaysia"] = data_T["Malaysia"].apply(clSuf).astype('float')
        # # Set axis steps and lable
        ax = plt.gca()
        ax.set_xlabel('Year')
        ax.set_ylabel('Population')
        ax.set_title('Population Projections')
        # plt.xlabel('Year')
        # plt.ylabel('Population')
        # plt.title('Population Projections')
        # Edit the axis labelling
        formatter = FuncFormatter(format)
        plt.xticks(np.arange(0, 360, step=40))
        plt.yticks(np.arange(0, 1000000000, step=20000000))
        ax.yaxis.set_major_formatter(formatter)
        data_T.France.plot(legend=True, color='green')
        data_T.Malaysia.plot(legend=True, color='blue')
        ax.legend(loc='lower right')
        # plt.legend(loc='lower right')
        plt.show()
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    """Testing"""
    main()
