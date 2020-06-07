import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://mahj00n.wordpress.com/')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='entry-header')

with open('blogposts.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Link', 'Last Updated']
  csv_writer.writerow(headers)

  for post in posts:
    title = post.find(class_='entry-title').get_text()
    link = post.find('a')['href']
    date = post.select('.updated')[0].get_text()
    csv_writer.writerow([title, link, date])