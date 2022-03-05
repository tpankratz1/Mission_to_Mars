#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


slide_elem.find('div', class_='content_title')


# In[7]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images 

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[12]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[13]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[14]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[15]:


df.to_html()


# In[16]:


browser.quit()


# In[ ]:





# In[17]:


# Challenge Starter Code


# In[18]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[19]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # Visit the NASA Mars News Site

# In[20]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[21]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[22]:


slide_elem.find('div', class_='content_title')


# In[23]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[24]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

# In[25]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[26]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[27]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[28]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[29]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# In[30]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[31]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[32]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ## Hemispheres

# In[33]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[34]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Find the HTML tag that holds all the links to the full-resolution images
html = browser.html
list_soup = soup(html, 'html.parser')
mars_hemisphere = list_soup.find_all('div', class_='description')

# Using a for loop, iterate through the tags
for x in range(len(mars_hemisphere)):
    
    # Create an empty dictionary
    hemispheres = {}
    
    # a) click on each hemisphere link
    browser.find_by_tag("h3")[x].click()
    
    # Parse the resulting html with soup
    html = browser.html
    hemispheres_soup = soup(html, 'html.parser')
    
    # Find the title
    title = hemispheres_soup.find("h2").text
    
    # Find the relative image url
    download_box = hemispheres_soup.find('div', class_='downloads')
    ul = download_box.find("ul")
    li = ul.find("li")
    a = li.find("a")
    image_url_rel = a["href"]
    
    # Find the full url by appending the relative image url to the main url
    img_url = url+image_url_rel

    # Save the full-resolution image URL string as the value for the img_url key ... 
    # ... that will be stored in the dictionary
    hemispheres["img_url"] = img_url
    
    # Save the hemisphere image title as the value for the title key ...
    # ... that will be stored in the dictionary
    hemispheres["title"] = title
        
    # Add the hemispheres dictionary with the image URL string and the hemisphere image title ...
    # ... to hemisphere_image_urls list
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# In[35]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[36]:


# 5. Quit the browser
browser.quit()

