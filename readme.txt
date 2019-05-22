All necessary datasets for a "Software Engineer" job title are included in the project zip file:
    CoLData.csv
    Indeed Salaries with Cities Clean.csv

Note: all necessary datasets can be obtained from the salary.py script, but scraping this data can
take a few hours.

Steps to run ASP (AI for Salary Prediction):
1. run "pip install -r requirements.txt"
1. run main.py (either from an IDE or from terminal)
2. The application will prompt you to enter a city (it will list valid cities you may choose from).
    Note: if you enter an invalid city, the application will keep prompting the user until a valid city is entered.
3. The application will prompt you to enter a job title
    NOTE: IF YOU WANT TO AVOID AN HOUR WAITING FOR THE APPLICATION TO SCRAPE SALARIES, enter "Software Engineer" for the
    title
4. The application will prompt you for your years of experience. If you enter a non-number, the application will default
    to 0 years of experience.
5. program will output results of the linear regression and its salaryprediction

Developer notes:
Prototyped front-end web application designs and logos are available for viewing in the templates directory.