from functional import seq

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