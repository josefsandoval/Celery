import math
import pandas as pd

class Person:
    def __init__(self, city, jobTitle, yearOfExperience, salary):
        self.city = city
        self.jobTitle = jobTitle
        self.yearOfExperience = yearOfExperience
        self.salary = salary


class KB:
    def findCoL(self, city):
        cost_of_living_data = pd.read_csv("ColData.csv")
        # get first row
        colCitiesList = cost_of_living_data.iloc[:, 0].tolist()
        index = colCitiesList.index(city)
        return cost_of_living_data.iloc[index, 2]

    def percentageByExperience(self, yearOfExperience):
        if yearOfExperience >= 0 and yearOfExperience <= 5:
            return -10
        elif yearOfExperience > 5 and yearOfExperience < 15:
            return 5
        elif yearOfExperience >= 15 and yearOfExperience < 25:
            return 19
        elif yearOfExperience >= 25:
            return 28

    def predictSalary(self, person):
        percentage = self.percentageByExperience(person.yearOfExperience)
        salaryByExperience = 0
        salary = person.salary

        if percentage >= 0:
            salaryByExperience = (salary * (1 + (percentage / 100)))
            return salaryByExperience
        else:
            salaryByExperience = (salary * (1 - (percentage / 100)))
            return salaryByExperience

        return salaryByExperience

