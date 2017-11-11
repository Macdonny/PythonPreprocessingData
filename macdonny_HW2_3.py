import pandas as pd
from pandas import DataFrame
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt
import seaborn as sns

quantitative_df = pd.read_csv('resources/quantitative.csv')
q_transferred_df = DataFrame()
outliers_row_df = DataFrame()

for(name, series) in quantitative_df.iteritems():
    q3 = series.quantile(.75)
    q1 = series.quantile(.25)
    median = series.median()
    iqr = q3 - q1

    print('-- ' + name + ' Upper and Lower Quartiles')
    upper = (median + (1.5 * iqr))
    lower = (median - (1.5 * iqr))

    print('upper quartiles: ', upper)
    print('lower quartiles: ', lower, '\n')

    outliers = []
    outliers_row = []
    # Check for outliers and track their indices
    for index, value in enumerate(series):
        if value > upper or value < lower:
            outliers.append(value)
            outliers_row.append(index)

    print('-- ' + name + ' Outliers')
    if not outliers:
        print('No Outliers', '\n')
    else:
        outliers_row_df[name] = pd.Series(outliers_row)

        outliers = np.array(outliers)
        print(outliers, '\n')

        print('-- Clamp Transformation')
        clamp_outliers = np.array(outliers)
        np.clip(outliers, lower, upper, out=clamp_outliers)

        print(clamp_outliers, '\n')
        clamp_outliers_df = DataFrame(clamp_outliers)

        print('-- Z-Score Normalization')
        normalized_clamp_outliers_df = clamp_outliers_df.apply(zscore)
        print(normalized_clamp_outliers_df)

        # Store transformed values back into quantitative DataFrame
        for key, i in clamp_outliers_df.iterrows():
            quantitative_df.at[key, name] = i

        q_transferred_df[name + '_ClampedValues'] = clamp_outliers_df[0]
        q_transferred_df[name + '_ClampNormalizedValues'] = normalized_clamp_outliers_df[0]
        print('-- Q Transferred DataFrame \n', q_transferred_df)

q_transferred_df.to_csv('resources/QTransferred.csv', index=False, encoding='utf-8')

quantitative_df = quantitative_df.apply(zscore) 
print('Outliers rows: \n', outliers_row_df)

for (name, series) in quantitative_df.iteritems():
    """
    Summary Table in Data Quality Report
    """
    print(name+"'s", "Summary Table in Data Quality Report")
    print("-- COUNT:", series.count())
    print("-- MISS %:", series.isnull().values.ravel().sum()/series.count())
    cardinality = series.unique()
    print("-- CARDINALITY:", cardinality.size)
    print("-- MIN VALUE:", series.min())
    print("-- 1st QRT VALUE:", series.quantile(.25))
    print("-- MEDIAN VALUE:", series.median())
    print("-- 3rd QRT VALUE:", series.quantile(.75))
    print("-- MAX VALUE:", series.max())
    print("-- MEAN VALUE:", series.mean())
    print("-- ST.DEV. VALUE:", series.std())
    print("-- VARIANCE VALUE:", series.var(), "\n")
    # Box Plot
    plt.boxplot(quantitative_df[name], vert=False)
    plt.savefig('resources/box_plots/part_3/' + name + '_box_plot_part_3')
    # plt.show()

"""
Scatter Plot Matrix
"""
df = pd.read_csv('resources/dataPreP.csv')
label = df['Labels']
scatter_plot_df = quantitative_df
scatter_plot_df['Labels'] = label
sns.set(style='ticks')
ax_sns_pp = sns.pairplot(scatter_plot_df, hue='Labels', palette="husl")
ax_sns_pp.savefig('resources/scatter_plots/scatter_plot_matrix_part_3')

