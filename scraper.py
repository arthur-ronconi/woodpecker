from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
import requests
import os

url = 'http://www.randomkittengenerator.com/cats/'

request = ureq(url)
pageHtml = request.read()

pageSoup = soup(pageHtml, "html.parser")

fileList = []
linkList = []

links = pageSoup.findAll("a")

for a in links:
    fileList.append(a["href"])

for i in range(5):
  del fileList[0]

for i in range(2):
  del fileList[len(fileList) - 1]
# print(len(fileList)-1)

for i in fileList:
  linkList.append(url + i)

path = os.getcwd()
os.chdir(path + '/img')
for i in range(len(linkList)):
    
    with open(fileList[i], 'wb') as handle:
      response = requests.get(linkList[i], stream=True)

      if not response.ok:
            print(response)

      for block in response.iter_content(1024):
          if not block:
              break

          handle.write(block)
os.chdir(path)
request.close()
