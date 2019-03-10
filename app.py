# Título, fecha, link y texto completo de la nota
from urllib.request import urlopen
from bs4 import BeautifulSoup
from functional import seq

from lib.archive import get_archive_list
from lib.posts import get_posts_from_year, get_post_text, add_description_to_dict
from lib.soup import get_soup_from_link, get_description_soup

fb_page = 'https://newsroom.fb.com/news'

page = urlopen(fb_page)
soup = BeautifulSoup(page, 'html.parser')

info_dictionary = (seq(get_archive_list(soup))
  .map(lambda link_dict: get_soup_from_link(link_dict.get('link'))) # Sirve que la consulta es más sencilla y puedes filtrar por fecha
  .map(lambda soup: get_posts_from_year(soup))
  .map(lambda post: add_description_to_dict(post)))

for cosa in info_dictionary:
  print('-'*20)
  print(cosa)
  print('-'*20)
