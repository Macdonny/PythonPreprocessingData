import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

quantitative_df = pd.read_csv('resources/quantitative.csv')
bins_df = DataFrame()
for(name, series) in quantitative_df.iteritems():
    equal_freq_sort = series.sort_values()
    equal_freq_df = equal_freq_sort.reset_index(drop=True)

    bin_count = 0
    bins_list = []
    bins = 1
    for (name2, value) in equal_freq_df.iteritems():
        bin_count = bin_count + 1
        if bin_count % 50 == 0:
            bins_list.append(value)
            bins_df['bin_' + str(bins)] = bins_list
            bins = bins + 1
            bins_list = []
        else:
            bins_list.append(value)
    ax = bins_df.plot.hist(bins=bins)
    ax.set_title('Attribute: ' + quantitative_df[name].name + '- Histogram with 10 Bins')
    ax.set_xlabel(quantitative_df[name].name)
    ax.set_ylabel('Count')
    fig = ax.figure
    fig.set_size_inches(8, 3)
    fig.tight_layout(pad=1)
    fig.savefig('resources/histogram_plots_part_5/' + quantitative_df[name].name + ' 10 Bins.png', dpi=600)
    plt.close(fig)

quantitative_binned_df = pd.merge(left=quantitative_df, right=bins_df, how='outer', left_index=True, right_index=True)
quantitative_binned_df.to_csv('resources/quantitativeBinned.csv', index=False, encoding='utf-8')
