from load_csv import load
import matplotlib.pyplot as plt
# import matplotlib.colors as col
from matplotlib.ticker import FuncFormatter
# import numpy as np
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
    return (x)


def main():
    try:
        year = 1900
        df1 = load('life_expectancy_years.csv')
        df2 = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        assert df1 is not None, "File Does Not Exist/wrong type"
        assert df2 is not None, "File Does Not Exist/wrong type"
        dropYear(df1, year, year)
        dropYear(df2, year, year)
        # Using plot instead of scatter
        # for i in df1.columns[1:]:
        #     df1.rename(columns={i:i + "_life"}, inplace=True)
        # for i in df2.columns[1:]:
        #     df2.rename(columns={i:i + "_gdp"}, inplace=True)
        # df = pd.merge(left=df1, right=df2, left_on='country',
        #               right_on='country')
        # for i in df.columns[1:]:
        #     df[i] = df[i].apply(clSuf).astype('float')
        # # Set axis steps and lable
        # df.plot(x=str(year) + '_gdp', y=str(year) + '_life', kind='scatter')
        ax = plt.gca()
        formatter = FuncFormatter(format)
        ax.set_xlabel('Gross domesic product')
        ax.set_ylabel('Life expectancy')
        ax.set_title(str(year))
        # ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=300))
        plt.xscale("log")
        # plt.xticks([300, 1000, 10000],["300", "1k", "10k"])
        # plt.tick_params(axis='x', which='minor', labelsize=10)
        ax.xaxis.set_major_formatter(formatter)
        plt.scatter(x=df2[str(year)], y=df1[str(year)])
        plt.show()
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    """Testing"""
    main()
