import salary as salary
import linear_model as lm
import KnowledgeBase as kb

cities = ['San Jose', 'San Francisco', 'San Diego', 'Los Angeles', 'Portland', 'Seattle', 'Chicago',
          'Dallas', 'Houston', 'Boston', 'Baltimore', 'Atlanta', 'New York', 'Columbus', 'Washington',
          'Denver', 'Huntsville']

job_title = ['Software', 'Computer Science']

if __name__ == '__main__':
    #take in user input, default user salary == 0
    userCity = input("Enter a Location (San Jose, San Francisco, San Diego, Los Angeles, Portland, \n"
                         "Seattle, Chicago, Dallas, Houston, Boston, Balitmore, Atlanta, New York, \n"
                         "Columbus, Washington, Denver, or Huntsville):")
    #input validation
    while not cities.__contains__(userCity):
        userCity = input("\nError, select one of the following locations: San Jose, San Francisco, San Diego, Los Angeles, Portland, \n"
                         "Seattle, Chicago, Dallas, Houston, Boston, Balitmore, Atlanta, New York, \n"
                         "Columbus, Washington, Denver, or Huntsville: ")

    #take in user job title
    userJobTitle = input("Enter a job title you want to predict a salary for: ")

    #get years of experience
    userYOE = int(input("Enter your years of experience:"))

    #input validation

    user = kb.Person(userCity, userJobTitle, userYOE, 0)

    has_data = False
    #scrape data if necesasry
    for title in job_title:
        if str(user.jobTitle).__contains__(title) and not(has_data):
            has_data = True

    if not has_data:
        salary.scrape_indeed(cities, user.jobTitle, 'Indeed Salaries with Cities.csv')
        salary.clean_up_salaries('Indeed Salaries with Cities.csv', 'Indeed Salaries with Cities Clean.csv')

    # get linear regression model
    linear_reg_model = lm.get_linear_model()

    #initialize knowledge base
    kb1 = kb.KB()

    #find corresponding cost of living for user
    costOfLiving = kb1.findCoL(user.city)
    #user.salary = linear_reg_model.predict([[costOfLiving]])

    #ask KB for correct percentage change according to experience
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



