import requests
from bs4 import BeautifulSoup

url = input("What is the url address of the twitter account?")
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'lxml')
try:
    follow_box = soup.find(
        'li',
        {'class': 'ProfileNav-item ProfileNav-item--followers'})
    followers = follow_box.find('a').find(
        'span',
        {'class': 'ProfileNav-value'})
    print(
        "The number of followers of this account is: {} ".
        format(followers.get('data-count')))
except:
    print('Account name not found...')
