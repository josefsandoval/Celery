
# no need to standardize because we only have one type of numeric data.
# normalization 0 ≤ z ≤ 1

from sklearn import preprocessing
import numpy as np
import pandas as pd


# all_csv = ['Indeed Salaries Clean_Austin.csv', 'Indeed Salaries Clean_Chicago.csv', 'Indeed Salaries Clean_New York.csv', 'Indeed Salaries Clean_Seattle.csv']
all_csv = ['Indeed Salaries Clean_Chicago.csv', 'Indeed Salaries Clean_New York.csv', 'Indeed Salaries Clean_Seattle.csv']
for csv in all_csv:
    df = pd.read_csv(csv)
    # Normalize total_bedrooms column
    x_array = np.array(df['Salary'])
    normalized_X = preprocessing.normalize([x_array])

    print('\n',csv,'\n', normalized_X, '\n')



# https://machinelearningmastery.com/prepare-data-machine-learning-python-scikit-learn/
# https://medium.com/@rrfd/standardize-or-normalize-examples-in-python-e3f174b65dfc

