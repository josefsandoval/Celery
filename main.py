import linear_model as lm
import KnowledgeBase as kb


if __name__ == '__main__':
    #take in user input, default user salary == 0
    user = kb.Person("San Jose", "Software Engineer", 12, 0)

    # get linear regression model
    linear_reg_model = lm.get_linear_model()

    #initialize knowledge base
    kb1 = kb.KB()

    #find corresponding cost of living for user
    costOfLiving = kb1.findCoL(user.city)

    #ask KB for correct percentage change according to experience, update salary for user
    #user = kb.Person(userLoc, userJob, userYOE, linear_reg_model.predict())
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



