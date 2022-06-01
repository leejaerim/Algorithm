import os
import csv
import requests
#from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

def get_site_url(s:str)->list:
  alba = requests.get(alba_url)
  soup = BeautifulSoup(alba.text,"html.parser")
  impact = soup.find("div",{"id":"MainSuperBrand"}).find_all("li",{"class":"impact"})
  sites= []
  for i in impact:
    sites.append(i.find("a"))
  return sites

def get_site_page(s:str)->int:
  try:
    pages = 0
    #test_url = "https://abcmart.alba.co.kr/"
    alba = requests.get(s)
    soup = BeautifulSoup(alba.text,"html.parser")
    pagination = soup.find("div",{"id":"SubContents"})
    jobCount = int(pagination.find("div",{"id":"NormalInfo"}).find("p",{"class":"jobCount"}).find("strong").get_text())
    if jobCount%50 == 0:
      pages = jobCount//50
    else:
      pages = jobCount//50 + 1
    return pages
  except:
    return 1

def get_jobs_from_url(s:str)->list:
  result = []
  #URL= "https://abcmart.alba.co.kr/job/brand/main.asp?page=3&pagesize=50"
  res = requests.get(s)
  soup = BeautifulSoup(res.text,"html.parser")
  info = soup.find("div",{"id":"NormalInfo"})
  tr = info.find_all("tr")
  for i in tr:
    if i.find("td",{"class":"local"}) is not None :
      local = i.find("td",{"class":"local"}).get_text()
      date = i.find("td",{"class":"data"}).get_text()
      pay = i.find("td",{"class":"pay"}).get_text()
      regDate = i.find("td",{"class":"regDate"}).get_text()
      title = i.find("td",{"class":"title"}).find("span",{"class":"company"}).get_text()
      result.append({
        'local':local,'title':title,'date':date,'pay':pay,'regDate':regDate
      })
  return result
  
def save_to_file(fn:str,jobs:list)->None:
  file  = open(f"{fn}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerows(["title","test"])
  #for job in jobs:
    #writer.writerows(job.values())

    
# site_url = get_site_url(alba_url)
# #for i in site_url:
# i = site_url[0]
# fn = i.find("span",{"class":"company"}).get_text()
# jobs = []
# for j in range(1,get_site_page(i["href"])+1):
#   url = i["href"]+"job/brand/main.asp?page="+str(j)+"&pagesize=50"
#   jobs += get_jobs_from_url(url)
# save_to_file(fn,jobs)







with open("cities.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "City", "Country"])
    writer.writerow(["1", "Seoul", "Korea"])
    writer.writerow(["1", "Tokyo", "Japanese"])