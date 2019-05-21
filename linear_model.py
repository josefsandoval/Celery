import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

salaries = pd.read_csv('Indeed Salaries with Cities Clean.csv', index_col=0).reset_index(drop=True)

cities_states = []
for location in salaries.Location:
    # We are only interested in the city and state of the job posting
    city_state = re.split('(\\d+)', location)[0].strip()
    cities_states.append(city_state)

# replace all locations we want to get rid of the zip Code and extra stuff
salaries['Location'] = cities_states


location_dummies = pd.get_dummies(salaries.Location).iloc[:, 1:]

merged = pd.concat([salaries, location_dummies], axis='columns')


final = merged.drop(['Location', 'Job_Title', 'Company'], axis='columns')

# print(final.head())
X = final.drop(['Salary'], axis='columns')
Y = final.Salary

salaries.plot(x ='Location', y='Salary', style='o')
plt.title('Location vs Salary')
plt.xlabel('Location')
plt.ylabel('Salary')
# plt.show()

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=58)
regr_model = LinearRegression()
regr_model.fit(x_train, y_train)

print("R2 Score:", regr_model.score(x_test, y_test))

y_pred = regr_model.predict(x_test)
print("lr.coef_: {}".format(regr_model.coef_))
print("lr.intercept_: {}".format(regr_model.intercept_))
print("Training set score: {:.2f}".format(regr_model.score(x_train, y_train)))
print("Test set score: {:.3f}".format(regr_model.score(x_test, y_test)))

# print(y_pred)
# df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred.round(2)})