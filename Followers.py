import requests
from BeautifulSoup import BeautifulSoup

url = unicode(input("What is the url address of the twitter account?"))
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('li', class_="ProfileNav-item--followers")
print table.prettify()
