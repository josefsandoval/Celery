import math

class Person:
    def __init__(self, city, jobTitle, yearOfExperience, salary):
        self.city = city
        self.jobTitle = jobTitle
        self.yearOfExperience = yearOfExperience
        self.salary = salary


class KB:
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






if __name__ == '__main__':

    kb1 = KB()
    user = Person("San Jose", "Software Engineer", 12, 120000)
    predictedSalary = 0
    predictedSalary = kb1.predictSalary(user)

    print( "Initial Salary: " )
    print(user.salary)
    print("      The AI predicted salary for a ")
    print(user.jobTitle)
    print(" in ")
    print(user.city)
    print(" with ")
    print(user.yearOfExperience)
    print(" years of experience is: ")
    print(predictedSalary)
