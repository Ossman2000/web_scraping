import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

company_name = []
job_title = []
location = []
skill = []
links=[]
salary=[]

result = requests.get("https://wuzzuf.net/search/jobs/?q=java&a=navbl")
src=result.content
soup=BeautifulSoup(src,"lxml")

job_titles = soup.find_all('h2',{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
locations = soup.find_all("span",{"class":"css-5wys0k"})
skills = soup.find_all("div",{"class":"css-y4udm8"})



for i in range (len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find('a').attrs['href'])
    company_name.append(company_names[i].text)
    location.append(locations[i].text)
    skill.append(skills[i].text)
    


for link in links :
    result = requests.get(link)
    src=result.content
    soup=BeautifulSoup(src,"lxml")
    salaries=soup.find("span",{"class":"css-wn0avc"})
    salary.append(salaries.text.strip())

file_list=[job_title,company_name,location,skill,links,salary]
exported=zip_longest(*file_list)
csv_file_path = "C:\\Users\\16092\\Documents\\A_MYPROJECTS\\webscrping\\joblisting.csv"
with open(csv_file_path ,'w') as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["job title","company Name","location","skills",'links','Salary'])
    wr.writerows(exported)

