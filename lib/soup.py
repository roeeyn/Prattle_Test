from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_soup_from_link(link):
  page = urlopen(link)
  return BeautifulSoup(page, 'html.parser')