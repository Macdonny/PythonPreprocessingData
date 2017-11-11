import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

quantitative_df = pd.read_csv('resources/quantitative.csv')

for(name, series) in quantitative_df.iteritems():
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
    plt.savefig('resources/box_plots/part_2/' + name + '_box_plot_part_2')
    plt.show()

    """
    Equal-Width Histogram
    """
    count, division = np.histogram(series, bins=np.linspace(series.min(), series.max(), 12))
    print(name+"'s", "Equal-Width Histogram")
    print('-- Borders of Bins:', division)
    print('-- Frequency of respective bins:', count)
    ax = quantitative_df[name].plot.hist(bins=division)
    ax.set_title('Attribute: ' + quantitative_df[name].name + '- Histogram with 12 Bins')
    ax.set_xlabel(quantitative_df[name].name)
    ax.set_ylabel('Count')
    fig = ax.figure
    fig.set_size_inches(8, 3)
    fig.tight_layout(pad=1)
    fig.savefig('resources/histogram_plots/' + quantitative_df[name].name + ' 12 Bins.png', dpi=600)
    plt.close(fig)

    """
    Horizontal Violin Plot
    """
    sns.set_style('whitegrid')
    ax_sns = sns.violinplot(x=quantitative_df[name])
    fig_sns = ax_sns.figure
    fig_sns.savefig('resources/violin_plots/' + quantitative_df[name].name)
    plt.close(fig_sns)


"""
Pair-Wise Analyses
"""
df = pd.read_csv('resources/dataPreP.csv')
pair_wise_df = DataFrame()

for(name, series) in df.iteritems():
    if series.dtype != 'object' or name == 'Labels':
        pair_wise_df[name] = series

"""
Scatter Plot Matrix
"""
sns.set(style='ticks')
ax_sns_pp = sns.pairplot(pair_wise_df, hue='Labels', palette="husl")
ax_sns_pp.savefig('resources/scatter_plots/scatter_plot_matrix_part_2')

"""
Covariance and Covariance Heatmap
"""
# Covariance Table
covariance = pair_wise_df.cov()
print("-- Covariance Table")
print(covariance)

# Covariance Heatmap
ax_sns_cov_heatmap = sns.heatmap(covariance)
figure_cov_heatmap = ax_sns_cov_heatmap.get_figure()
figure_cov_heatmap.savefig('resources/heatmaps/covariance_heatmap')

"""
Correlation Table and Correlation Heatmap
"""
# Correlation Table
correlations = pair_wise_df.corr()
print("-- Correlation Table")
print(correlations)

# Correlation Heatmap
ax_sns_corr_heatmap = sns.heatmap(correlations)
figure_corr_heatmap = ax_sns_corr_heatmap.get_figure()
figure_corr_heatmap.savefig('resources/heatmaps/correlation_heatmap')
