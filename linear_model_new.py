import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

salaries = pd.read_csv('Indeed Salaries with Cities Clean.csv', index_col=0).reset_index(drop=True)

X = salaries['Cost of Living'].values.reshape(-1, 1) # Independent var
Y = salaries.Salary # Dependent var, what we are predicting

def get_model():
    '''
    Run Training on our X and Y
    80% of data for training
    20% for validation/testing
    '''
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=58)
    regr_model = LinearRegression()
    regr_model.fit(x_train, y_train)

    y_pred = regr_model.predict(x_test)
    print("lr.coef_: {}".format(regr_model.coef_))
    print("lr.intercept_: {}".format(regr_model.intercept_))
    print("Training set score: {:.2f}".format(regr_model.score(x_train, y_train)))
    # % of the variability that Y(Salary) can be explained using X(Location)
    print("Test set score(R2): {:.3f}".format(regr_model.score(x_test, y_test)))

    plt.scatter(x_test, y_test, color='red')
    plt.plot(x_train, regr_model.predict(x_train), color='blue')
    plt.title('Salary vs Cost of Living (Test set)')
    plt.xlabel('Cost of Living')
    plt.ylabel('Salary')
    # plt.show() # Show the plot

    # # supposed users input of their cost of living
    # cost_of_living = 13.87
    #
    # # Here we predict based on the user input
    # print('\nPredicted Salary for {}(Cost of Living) is:'.format(cost_of_living),
    #       regr_model.predict([[cost_of_living]]))

    return regr_model
