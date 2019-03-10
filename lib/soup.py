from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_soup_from_link(link):
  page = urlopen(link)
  return BeautifulSoup(page, 'html.parser')

def get_description_soup(post):
  soup = get_soup_from_link(post.get('link'))
  post['description'] = soup
  return post