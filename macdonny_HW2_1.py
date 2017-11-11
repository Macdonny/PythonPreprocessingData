import pandas as pd
from pandas import DataFrame

df = pd.read_csv('resources/dataPreP.csv')
quantitative_df = DataFrame()
other_df = DataFrame()

for(name, series) in df.iteritems():
    if series.dtype != 'object':
        quantitative_df[name] = series
    else:
        other_df[name] = series

quantitative_df.to_csv('resources/quantitative.csv', index=False, encoding='utf-8')
other_df.to_csv('resources/other.csv', index=False, encoding='utf-8')
