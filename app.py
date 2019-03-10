# Título, fecha, link y texto completo de la nota
from urllib.request import urlopen
from bs4 import BeautifulSoup
from functional import seq
import pandas as pd

from lib.archive import get_archive_list
from lib.posts import get_posts_from_year, get_post_text, add_description_to_dict, filter_link_by_year
from lib.soup import get_soup_from_link, get_description_soup

fb_page = 'https://newsroom.fb.com/news'

page = urlopen(fb_page)
soup = BeautifulSoup(page, 'html.parser')

# Date Format - December 15, 2013
initialDate = { "day": 1, "month": 12, "year": 2017 }
endingDate = { "day": 1, "month": 12, "year": 2019 }

print('Fetching data...')
info_dictionary = (seq(get_archive_list(soup)) # Bring all years available in 'Archivo' section
  .filter(lambda link: filter_link_by_year(link.get('link'), initialDate, endingDate))
  .map(lambda link_dict: get_soup_from_link(link_dict.get('link'))) # While we fetch all years, it's better for filtering the years
  .map(lambda soup: get_posts_from_year(soup))
  .flat_map(lambda post: add_description_to_dict(post)))
print('Finished fetching data')

print('Started to create data Frame...')
data_frame = pd.DataFrame(info_dictionary)
print('Finished creating data Frame')

print('Saving data frame to csv...')
data_frame.to_csv('posts.csv', encoding='utf-8')