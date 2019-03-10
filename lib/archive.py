from functional import seq

def get_archive_list(soup):
  widgets = soup.find_all('div', class_='sidebar-widget')
  return (seq(widgets)
    .filter(lambda widget: widget.find('h2').string == 'Archive')
    .flat_map(lambda archive: archive.find_all('a'))
    .map(lambda anchor: anchor.get('href')))