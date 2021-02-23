import requests

url='https://ipinfo.io/countries/us' #Enter your URL
from bs4 import BeautifulSoup

html_content = requests.get(url).text
soup = BeautifulSoup(html_content,"lxml")
data = soup.find_all("td",attrs="p-3") #This line means go every td wich contains p-3 attribute and take all data. 

listofdata = []
for link in data:
    listofdata.append(link.text)
MyList=[s for s in listofdata if "AS" in s]# And this line works like some kind of filter for me.

print(MyList)