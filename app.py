# Título, fecha, link y texto completo de la nota
from urllib.request import urlopen
from bs4 import BeautifulSoup
from functional import seq

from lib.archive import get_archive_list
from lib.posts import get_posts_from_year, get_post_text
from lib.soup import get_soup_from_link

def get_description_soup(post):
  soup = get_soup_from_link(post.get('link'))
  post['description'] = soup
  return post

def add_description_to_dict(year_posts):
  return (seq(year_posts)
    .map(lambda post: get_description_soup(post))
    .map(lambda post: get_post_text(post)))

fb_page = 'https://newsroom.fb.com/news'

page = urlopen(fb_page)
soup = BeautifulSoup(page, 'html.parser')

archive_list_links = (seq(get_archive_list(soup))
  .map(lambda link_dict: get_soup_from_link(link_dict.get('link'))) # Sirve que la consulta es más sencilla y puedes filtrar por fecha
  .map(lambda soup: get_posts_from_year(soup))
  .map(lambda post: add_description_to_dict(post)))

for cosa in archive_list_links:
  print('-'*20)
  print(cosa)
  print('-'*20)
