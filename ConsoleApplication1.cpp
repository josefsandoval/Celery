// ConsoleApplication1.cpp 
//	This is a way to represent the KB and calculate the salatu by years of experince
//	For this to work we need to compute the predicted salary 

#include <iostream>
#include <string>

using namespace std;

class Person {
public:
	string city;
	string jobTitle;
	int yearOfExperience;
	int salary;

	Person(string iCity,
	string iJobTitle,
	int iYearOfExperience,
	int iSalary) {
		city = iCity;
		jobTitle = iJobTitle;
		yearOfExperience = iYearOfExperience;
		salary = iSalary;
	}
};

class KB {

public:

	int predictSalary(Person person);

	//This is base on the data provided by https://www.payscale.com/research/US/Job=Software_Engineer/Salary
	float percentageByExperience(int yearOfExperience);

};


int KB::predictSalary(Person person) {

	float percentage = percentageByExperience(person.yearOfExperience);
	int salaryByExperience = 0;
	int salary = person.salary;

	if (percentage >= 0) {
		salaryByExperience = (salary * (1 + (percentage / 100)));
		return salaryByExperience;
	}
	else {
		salaryByExperience = salary * (1 - (percentage / 100));
		return salaryByExperience;
	}

	return salaryByExperience;

}

float KB::percentageByExperience(int yearOfExperience) {

	//Entry-Level
	if (yearOfExperience >= 0 && yearOfExperience <= 5)
		return -10;
	//Mid-Career
	else if (yearOfExperience > 5 && yearOfExperience < 15)
		return 5;
	//Experienced
	else if (yearOfExperience >= 15 && yearOfExperience < 25)
		return 19;
	//Late-Career
	else if (yearOfExperience >= 25)
		return 28;

}

int main()
{
	KB kb1;
	Person user =  Person("San Jose", "Software Engineer", 12, 120000);

	int predictedSalary = kb1.predictSalary(user);

	cout << "Initial Salary: " << user.salary << endl
		<< "The AI predicted salary for a " << endl
		<< user.jobTitle << " in " << user.city << " with " << user.yearOfExperience << " years of experience is: " << endl
		<< "\t" << predictedSalary << endl;


}
