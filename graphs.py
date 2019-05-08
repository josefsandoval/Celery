from sklearn import preprocessing
import numpy as np
import pandas as pd

# cannot plot histogram of strings, so this is bar plot.

def bar(df, name):
    plt.bar(df.Location, df.Salary, color = 'darkorange')
    plt.title(csv)
    plt.xticks(df.Location, rotation=89)
    plt.ylim(min(df.Salary), max(df.Salary))
    plt.show()
    plt.clf()

from matplotlib import pyplot as plt
all_csv = ['Indeed Salaries Clean_Chicago.csv', 'Indeed Salaries Clean_New York.csv', 'Indeed Salaries Clean_Seattle.csv']
for csv in all_csv:
    df = pd.read_csv(csv)
    all_groups = df.groupby(['Location'], as_index=False).mean()
    bar(all_groups, csv)
