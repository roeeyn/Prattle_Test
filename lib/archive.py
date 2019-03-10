from functional import seq

def get_year_and_link(anchor):
  return {"link": anchor.get('href')}

def get_archive_list(soup):
  widgets = soup.find_all('div', class_='sidebar-widget')
  return (seq(widgets)
    .filter(lambda widget: widget.find('h2').string == 'Archive')
    .flat_map(lambda archive: archive.find_all('a'))
    .map(lambda anchor: get_year_and_link(anchor)).to_list())