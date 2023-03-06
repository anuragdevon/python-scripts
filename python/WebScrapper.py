#!usr/bin/python

# important information!!
# query parameter begins with question mark
# they are separated by &
# key = value, pieces of information are encoded with key values pairs
# DOM - document object model

import requests
import pprint
from bs4 import BeautifulSoup

# getting the html from the site
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# above sends HTTP request to webpage and retrives the HTML data and stores in "python object"
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id = 'ResultsContainer')

# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)

# for job_elem in job_elems:
#     # each job_elem is a new BeautifulSoup object
#     # You can use the same methods on it as you did before
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')

#     # for handling the issues related to ads embeded within html
#     if None in (title_elem, company_elem, location_elem):
#         continue

#     # printing
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()

# now using filter to filter out specific jobs
# python_jobs = results.find_all('h2', string = 'Python Developer')
# using this will print black output as because if matching exact keyword
# so we should make the string more general

python_jobs = results.find_all('h2', string = lambda text: 'software' in text.lower())
print(len(python_jobs))

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"APPLY HERE: {link}\n")