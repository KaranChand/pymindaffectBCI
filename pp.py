import csv
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def pp():
    list_csv = glob.glob('csv/**/*.csv')
    dfs = []

    path_list = []

    for path in list_csv:
        path_list.append(path.split(os.sep))

    time = [path[1] for path in path_list]

    for i in (list_csv):
        df = pd.read_csv(i)
        dfs.append(df)

    column_names = dfs[0].columns.tolist()
    columns_names2 = dfs[4].columns.tolist()

    list_csv2 = glob.glob('csv/**/metadata.csv')

    mds = []

    for i in (list_csv2):
        md = pd.read_csv(i, index_col=False)
        mds.append(md)

    column_names3 = mds[0].columns.tolist()

    return dfs, column_names, columns_names2, column_names3, path_list, time, mds