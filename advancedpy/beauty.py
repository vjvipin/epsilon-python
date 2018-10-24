# 1 Beautiful Soup => library 
# 2 Scrapy => framework 

# pip install BeautifulSoup4
# pip install requests

# http://wwww.zekelabs.com


import requests 
from bs4 import BeautifulSoup

response = requests.get("http://www.zekelabs.com")
#response = requests.get("http://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore")

print(response.status_code)
print(response.content)
soup = BeautifulSoup(response.content,"html.parser")
#cards = soup.find_all("div",attrs={"class":"subject-title"})
cards = soup.find_all("img")

print(cards)
