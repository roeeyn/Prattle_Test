from functional import seq
from lib.soup import get_description_soup
from datetime import datetime

def get_month_number_from_string(string_month):
  return (
    1 if string_month == 'january'
    else 2 if string_month == 'february'
    else 3 if string_month == 'march'
    else 4 if string_month == 'april'
    else 5 if string_month == 'may'
    else 6 if string_month == 'june'
    else 7 if string_month == 'july'
    else 8 if string_month == 'august'
    else 9 if string_month == 'september'
    else 10 if string_month == 'october'
    else 11 if string_month == 'november'
    else 12 if string_month == 'december'
    else -1)

def get_date_dict_from_post(post):
  # Date Format - December 15, 2013
  processed_date = post["date"].replace(',', '').split()
  string_month = processed_date[0].lower()
  month_number = get_month_number_from_string(string_month)
  day = int(processed_date[1])
  year = int(processed_date[2])
  return { "day": day, "month": month_number, "year": year }

def filter_post_by_date(post, initial_date, ending_date):
  post_date_dict = get_date_dict_from_post(post)
  initial_datetime = datetime(initial_date["year"], initial_date["month"], initial_date["day"])
  ending_datetime = datetime(ending_date["year"], ending_date["month"], ending_date["day"])
  post_datetime = datetime(post_date_dict["year"], post_date_dict["month"], post_date_dict["day"])
  return initial_datetime <= post_datetime <= ending_datetime

def filter_link_by_year(link, initial_date, ending_date):
  link_year = int(link[-4:])
  return initial_date["year"] <= link_year <= ending_date["year"]

def get_post_text(post):
  post['description'] = post.get('description').find('div', class_='post-content')
  return post

def get_info_from_year_post(year_post):
  date = year_post.find('p', class_='date').string
  anchor = year_post.find('a')
  title = anchor.string.strip()
  link = anchor.get('href')
  return {"date": date, "title": title, "link": link}

def get_posts_from_year(soup):
  posts = soup.find(id='main').find_all('div', class_='article-summary')
  posts_info = (seq(posts)
    .map(lambda post: get_info_from_year_post(post)).to_list())
  return posts_info

def add_description_to_dict(year_posts):
  soup = get_description_soup(year_posts)
  return get_post_text(soup)