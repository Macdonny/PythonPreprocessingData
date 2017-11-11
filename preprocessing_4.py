import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

other_df = pd.read_csv('resources/other.csv')

for(name, series) in other_df.iteritems():
    """
    Summary Table in Data Quality Report
    """
    print(name+"'s", "Summary Table in Data Quality Report")
    print("-- COUNT:", series.count())
    print("-- MISS %:", series.isnull().values.sum()/series.count())
    cardinality = series.unique()
    print("-- CARDINALITY:", cardinality.size)

    mode = series.mode()
    print("-- MODE:", mode[0])

    group_count = series.value_counts()
    mode_f = group_count.max()
    print("-- MODE FREQUENCY:", mode_f)

    total = series.count()
    print("-- MODE %:", (mode_f/total) * 100)

    print(group_count)
    second_count = group_count.drop(mode[0])
    print(second_count)
    second_mode = second_count.to_frame()
    print("-- 2ND MODE:", second_mode.index[0])

    second_mode_f = second_count.max()
    print("-- 2ND MODE FREQUENCY:", second_mode_f)

    second_total = second_count.sum()
    print("-- 2ND MODE %:", (second_mode_f/second_total) * 100)
