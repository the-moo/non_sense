#!/bin/python3

"""
Webscraper made with the help of Realpython.com, remove commented out print commands to see parse change
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/" #URL of site (static site for educational use)
page = requests.get(URL) #copies HTML code of site

##print(page.text) #print HTML to check for successful import

soup = BeautifulSoup(page.content, "html.parser") #Use .content instead of .text for decoding reasons
results = soup.find(id="ResultsContainer") #area of desired focus
#print(results.prettify()) #prettify makes out put more user fiendly

job_elements = results.find_all("div", class_="card-content")
#for job_element in job_elements: #filering out selected fields
   # print(job_element, end="\n"*2) 
   #title_element = job_element.find("h2", class_="title")
   #company_element = job_element.find("h3", class_="company")
   #loaction_element = job_element.find("p", class_="location")
   #print(title_element.text.strip()) #use .text to filter out html and leave only desired text
   #print(company_element.text.strip()) #use .strip to remove uneeded white space
   #print(loaction_element.text.strip())
   #print()

python_jobs = results.find_all(
   "h2", string=lambda text: "python" in text.lower() #focus on keywords, use lambda to avoid letter case confusion
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs # needed to avoid error caused by empty returns, identifies parent of desired element
]

print(str(len(python_jobs)) + " jobs are avaliable" '\n' ) #shows number of jobs with keyword

for job_element in python_job_elements:
   title_element = job_element.find("h2", class_="title")
   company_element = job_element.find("h3", class_="company")
   loaction_element = job_element.find("p", class_="location")
   link_url = job_element.find_all("a")[1]["href"] #find index number of desired element (link)
   print(title_element.text.strip()) #use .text to filter out html and leave only desired text
   print(company_element.text.strip()) #use .strip to remove uneeded white space
   print(loaction_element.text.strip())
   print(f"Apply here: {link_url}\n") # use f to have link printed 
   print()
