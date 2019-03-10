# Título, fecha, link y texto completo de la nota
from urllib.request import urlopen
from bs4 import BeautifulSoup

from lib.archive import get_archive_list

fb_page = 'https://newsroom.fb.com/news'

page = urlopen(fb_page)
soup = BeautifulSoup(page, 'html.parser')
archive_list_links = get_archive_list(soup)
print(archive_list_links)

