from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import random
import pymongo
from time import sleep


def scrape():
    try:
        executable_path = {'executable_path': ChromeDriverManager().install()}
    except:
        # Specify the ChromeDriver version
        chrome_version = "114.0.5735.90"

        # Set up the executable path with the specified version
        executable_path = {'executable_path': ChromeDriverManager(version=chrome_version).install()}
        
    browser = Browser('chrome', **executable_path, headless=False)

    ## conn = 'mongodb://localhost:27017'
    ## client = pymongo.MongoClient(conn)
    client = pymongo.MongoClient("mongodb+srv://dbMarsUser:TerraMars95@mars-scraping.femkc.mongodb.net")
    db = client.mars_mission_db
    collection = db.mars
    collection.drop()

    url = 'https://redplanetscience.com/'

    try:
        browser.visit(url)
    except:
        sleep(5)
        browser.visit(url)

    news_title = []
    news_p = []

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    sleep(2)
    news = soup.find('section', class_='image_and_description_container')
    sleep(4)
    titles = news.find_all('div', class_='content_title')
    sleep(4)
    descriptions = news.find_all('div', class_='article_teaser_body')

    for title in titles:
        main_title = title.text
        news_title.append(main_title)

    for description in descriptions:
        main_description = description.text
        news_p.append(main_description)


    mars_url = 'https://spaceimages-mars.com/'
    try:
        browser.visit(mars_url)
    except:
        sleep(5)
        browser.visit(mars_url)
        
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    header = soup.find('div', class_='header')
    image =  header.find('img', class_='headerimage fade-in')
    featured_image_url = f'https://spaceimages-mars.com/{image["src"]}'


    mars_facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(mars_facts_url)
    mars_table_df = tables[0]

    mars_df  = mars_table_df.rename(columns = {0:'Description',1:'Mars',2:'Earth'})
    mars_df = mars_df.set_index('Description')
    mars_html_table = mars_df.to_html()
    mars_html_table


    mars_hemispheres_url = 'https://marshemispheres.com/'
    try:
        browser.visit(mars_hemispheres_url)
    except:
        sleep(5)
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

    links_list = []
    for t in titles_list:
        try:
            browser.visit(mars_hemispheres_url)
        except:
            sleep(5)
            browser.visit(mars_hemispheres_url)
        try:
            browser.links.find_by_partial_text(t).click()
        except:
            sleep(5)
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

    hemisphere_image_urls = []
    number = 0
    dict_len = len(list_of_urls)
    while number < dict_len:
        images_dict = {'title':titles_list[number],'img_url':list_of_urls[number]}
        hemisphere_image_urls.append(images_dict)
        number = number + 1

    lenght = len(news_title) - 1
    print(lenght)
    try:
        new_number = random.randint(0,lenght)
    except:
        sleep(2)
        new_number = random.randint(0,lenght)


    selected_title = news_title[new_number]
    selected_paragraph = news_p[new_number]

    cerberus_image = titles_list[0]
    cerberus_link = list_of_urls[0]
    schiaparelli_image = titles_list[1]
    schiaparelli_link = list_of_urls[1]
    syrtis_image = titles_list[2]
    syrtis_link = list_of_urls[2]
    valles_image = titles_list[3]
    valles_link = list_of_urls[3]

    scrap_values = {}
    scrap_values['News_Title'] = selected_title
    scrap_values['News_Paragraph']  = selected_paragraph
    scrap_values['Featured_Image_Url'] = featured_image_url
    scrap_values['Cerberus'] = cerberus_image
    scrap_values['Cerberus_Link'] = cerberus_link
    scrap_values['Schiaparelli'] = schiaparelli_image
    scrap_values['Schiaparelli_Link'] = schiaparelli_link
    scrap_values['Syrtis'] = syrtis_image
    scrap_values['Syrtis_Link'] = syrtis_link
    scrap_values['Valles'] = valles_image
    scrap_values['Valles_Link'] = valles_link

    collection.insert_one(scrap_values)

    browser.quit()

    return scrap_values
