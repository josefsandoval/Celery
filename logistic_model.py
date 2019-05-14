import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Here we will be using Classification using LogisticRegression
We want to classify whether a job will have and Above Median Salary
or a Below Median Salary based on the Jobs location and Job title description
'''

salaries = pd.read_csv('data/SalaryData.csv', index_col=0).reset_index(drop=True)

# Compute the median salary in the DataSet
median_salary = salaries.Salary.median()

'''
Create new DataSet column with a predictor value
We want to be able to classify whether a job is above or 
below the median based on the location and title
'''
salaries['Above_Median'] = [1 if salary > median_salary else 0 for salary in salaries.Salary]
# print(salaries.Location.value_counts())


'''
Clean up the locations, get rid of zip codes and extra parameters
We are only interested in City and State
'''

locations = []
for location in salaries.Location:
    locations.append(re.split('(\\d+)', location)[0].strip())
salaries.Location = locations
# plt.scatter(salaries.Location.head(20), salaries.Above_Median.head(20), marker='+', color='red')


# Dummy Encoding for Locations
dummy_encoded_salaries = pd.get_dummies(salaries.Location).iloc[:, 1:]

'''
Use a CountVectorizer to determine the frequency of key words in the job title
Setting up the CountVectorizer to only get key words that appear more than 1% of the time
'''
cv = CountVectorizer(stop_words='english', ngram_range=(1, 3), min_df=.001)

# return term-doc matrix
X_cv = cv.fit_transform(salaries.Job_Title)

# make new DataFrame from CountVectorizer results
job_title_cv_df = pd.DataFrame(X_cv.todense(), columns=cv.get_feature_names())
# print(job_title_cv_df)


# Print details of the titles and their occurrences
title_occurrences = job_title_cv_df.sum(axis=0)
print(title_occurrences.sort_values(ascending=False))

# the feature variable used for training (Independent variable)
X = pd.concat([dummy_encoded_salaries, job_title_cv_df], axis=1)
# predicting whether the salary will be above the median (Our dependent variable)
Y = salaries.Above_Median

'''
Run Training on our X and Y
70% of data for training
30% for validation/testing
'''
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=58, stratify=Y)
logistic_reg = LogisticRegression(solver='lbfgs')
logistic_reg.fit(x_train, y_train)

# Look at the accuracy of the model
predicted = logistic_reg.predict(x_test)
predicted_accuracy = accuracy_score(y_test, predicted)
print("Prediction Accuracy: ", predicted_accuracy.round(2))

s = cross_val_score(logistic_reg, x_train, y_train, cv=10, n_jobs=-1)
print("Cross Val Score: {:0.3} ± {:0.3}".format(s.mean().round(3), s.std().round(3)))

# visualizing the data
matrix = metrics.confusion_matrix(y_test, predicted)
class_names = [0, 1]  # name  of classes
fig, axis = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# heatmap
sns.heatmap(pd.DataFrame(matrix), annot=True, fmt='g')
axis.xaxis.set_label_position('bottom')
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()