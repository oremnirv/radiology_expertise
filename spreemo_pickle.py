import sys
import pandas as pd


def read_pkl_file(full_path):

    return pd.read_pickle(full_path)


def main():
    pkl_file = read_pkl_file("/Users/omer/Downloads/npis.pkl")


if __name__ == '__main__':
    main()