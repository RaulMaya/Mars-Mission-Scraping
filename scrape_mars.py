from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)

news_title = []
news_p = []

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

news = soup.find('section', class_='image_and_description_container')
titles = news.find_all('div', class_='content_title')
descriptions = news.find_all('div', class_='article_teaser_body')

for title in titles:
    main_title = title.text
    news_title.append(main_title)

for description in descriptions:
    main_description = description.text
    news_p.append(main_description)

n = len(news_p)
c = 0

while c < n:
    print(news_title[c])
    print(news_p[c])
    print('--------------')
    c = c + 1

mars_url = 'https://spaceimages-mars.com/'
browser.visit(mars_url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

header = soup.find('div', class_='header')
image =  header.find('img', class_='headerimage fade-in')
featured_image_url = f'https://spaceimages-mars.com/{image["src"]}'
print(featured_image_url)

mars_facts_url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(mars_facts_url)
mars_table_df = tables[0]
mars_table_df

mars_df  = mars_table_df.rename(columns = {0:'Description',1:'Mars',2:'Earth'})
mars_df = mars_df.set_index('Description')
mars_df

mars_html_table = mars_df.to_html()
mars_html_table

mars_hemispheres_url = 'https://marshemispheres.com/'
browser.visit(mars_hemispheres_url)

titles_list = []
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

container = soup.find('div', class_='container')
collapsible_results =  container.find('div', class_='collapsible results')
items  = collapsible_results.find_all('div',  class_='item' )
items_count = len(items)
for item in items:
    topic = item.find('div',class_='description')
    main_mh_titles = topic.find('h3').text
    titles_list.append(main_mh_titles)
titles_list

links_list = []
for t in titles_list:
    browser.visit(mars_hemispheres_url)
    browser.links.find_by_partial_text(t).click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    wrapper = soup.find('div', class_= 'wrapper')
    w_image = wrapper.find('div', class_= 'wide-image-wrapper')
    li = wrapper.find('li')
    a = li.find_all('a')
    for x in a:
        link = x['href']
        links_list.append(link)
list_of_urls = ['https://marshemispheres.com/' + key_url for key_url in links_list]
list_of_urls

hemisphere_image_urls = []
number = 0
dict_len = len(list_of_urls)
while number < dict_len:
    images_dict = {'title':titles_list[number],'img_url':list_of_urls[number]}
    hemisphere_image_urls.append(images_dict)
    number = number + 1

print(hemisphere_image_urls)

browser.quit()
