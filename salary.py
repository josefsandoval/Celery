from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

cost_of_living_data = pd.read_csv("ColData.csv")

# Helper functions to get the data from Indeed and Stack Overflow tags
def get_company(tag):
    try:
        return tag.find('span', {'class': 'company'}).text.strip()
    except:
        return None


def get_title(tag):
    try:
        return tag.find('a', {'class': 'turnstileLink'}).text.strip()
    except:
        return None


def get_salary(tag):
    try:
        return tag.find('span', {'class': 'salary'}).text.strip()
    except:
        return None


def get_location(tag):
    try:
        return tag.find('span', {'class': 'location'}).text.strip()
    except:
        return None


# End helper functions

# Get Job title
def get_title_so(job_post):
    try:
        return job_post.find('a', {'class': 's-link s-link__visited'}).text.strip()
    except:
        return None


# Get Company
def get_company_so(job_post):
    try:
        return job_post.find('div', {'class': '-company'}).contents[1].string.strip()
    except:
        return None


# Get Location
def get_location_so(job_post):
    try:
        return job_post.find('div', {'class': '-company'}).contents[3].string.replace('-', '').strip()
    except:
        return None


# Get Salary
def get_salary_so(job_post):
    try:
        return job_post.find('span', {'class': '-salary'}).text.replace('Equity', '').replace('|', '').strip()
    except:
        return None

#get cost of living
def get_cost_of_living(city):
    #get first row
    colCitiesList = cost_of_living_data.iloc[:, 0].tolist()
    index = colCitiesList.index(city)
    return cost_of_living_data.iloc[index, 2]


# Clean up salaries from out csv file to only include yearly incomes, remove any estimated salaries
# param1: csv file we want to clean, param2: cleaned/new csv file name
# Computes the Average Salary
def clean_up_salaries(csv_file, name='clean.csv'):
    salaries = pd.read_csv(csv_file, index_col=0).reset_index(drop=True)
    salaries.drop(salaries[(salaries.Salary.str.contains('week') | salaries.Salary.str.contains(
        'Indeed') | salaries.Salary.str.contains('estimate') | salaries.Salary.str.contains('hour')
                            | salaries.Salary.str.contains('day') | salaries.Salary.str.contains('month'))].index)
    # Compute the Average Salary
    computed_averages = []
    for salary_str in salaries.Salary:
        if 'k' in salary_str:
            salary_str = salary_str.replace('k', '000')
        salary_str = re.sub(r'[^\s\d]', '', salary_str)
        salaries_split = salary_str.strip().split()
        print(salaries_split)
        average = np.mean([float(n) for n in salaries_split])
        print("Computed Salary Avg: {}".format(average))
        computed_averages.append(average)

    salaries.Salary = computed_averages
    # dropping salaries that are obviously too low
    salaries.drop(salaries[salaries.Salary < 30000].index, inplace=True)
    salaries.to_csv('{}'.format(name))


# indeed does not show the actual mount of job posts requested, max they show per page is 57
# we want to keep results even, avg 50 job results per query
# first page: 0-44, second page: 44-88, third page: 88-132 etc... <-- each page will return 50 results.
# start range at 0 increment by 44 every time, this should give us ~1000 salary results total for our data
# (20 soups, each should contain avg. 50 results)
def scrape_indeed(cities, job_title, csv_file_name='Indeed Salaries.csv'):
    records = []
    max_results = 1320
    for title in job_title:
        for city in cities:
            print('Scraping salaries in {}'.format(city))
            soups = []
            # grab the results for every page, by setting limit to 44, indeed gives us ~50 results per page
            # every iteration we start at the next page: page 1(0-44), page 2(44-88)
            # want to grab around 1000 results per city, so set limit to 880
            for start in range(0, max_results, 44):
                url = 'https://www.indeed.com/jobs?as_and={}&as_phr=' \
                      '&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&' \
                      'radius=50&l={}&fromage=any&limit=44&start={}&sort=&psf=advsrch'.format(title, city, start)
                result = requests.get(url)
                soup = BeautifulSoup(result.text, 'html.parser')
                soups.append(soup)
                sleep(2)

            jobs = []
            for soup in soups:
                for job in soup.find_all('div', {'class': 'jobsearch-SerpJobCard unifiedRow row result'}):
                    jobs.append(job)

            print('{} jobs found near {}'.format(len(jobs), city))

            for job in jobs:
                records.append((get_title(job), get_company(job), city, get_salary(job), get_cost_of_living(city)))

    df = pd.DataFrame(records, columns=['Job_Title', 'Company', 'Location', 'Salary', 'Cost of Living'])
    # drop any data that has missing values, remove any duplicates that appear
    clean = df.dropna(how='any').drop_duplicates()
    # Export the DataFrame to a csv file
    clean.to_csv(csv_file_name)

