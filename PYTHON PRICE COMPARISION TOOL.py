#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from time import sleep
import requests
import time
import pandas as pd


# In[2]:


website_amazon_india="https://www.amazon.in/"

website_amazon_USA="https://www.amazon.co.uk/"


# In[3]:


options=Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument('--no-sandbox')
options.add_argument("--disable-site-isolation-trials")

path="M:\chromedriver.exe"
service=Service(executable_path=path)
browser=webdriver.Chrome(service=service,options=options)


# In[4]:


browser.get(website_amazon_india)


# In[5]:


search_item="lenovo legion 5"


# In[6]:


search_bar=browser.find_element(by='id',value="twotabsearchtextbox")


# In[7]:



search_bar.send_keys(search_item)


# In[8]:


search_button=browser.find_element(by='id',value="twotabsearchtextbox").submit()


# In[9]:


containers=browser.find_elements(
    by='xpath',value='//div[@class="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right"]//h2')


# In[10]:


link_containers=browser.find_elements(by='xpath',value='//div[@class="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right"]//h2/a')


# In[11]:


price_containers=browser.find_elements(by='xpath',value='//div[@class="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right"]//span[@class="a-price-whole"]')


# In[12]:


product_descriptions=[]
links=[]
prices=[]


# In[13]:


# (for container in containers:
     # if '(Renewed)' in container.text:
         #unwanted_element=container.text
        #cleaning_index=index
   # product_description=container.text
    #product_descriptions.append(product_description)
    #)


# In[14]:


for container in containers:
    product_description=container.text
    product_descriptions.append(product_description)


# In[15]:


for link_container in link_containers:
    link=link_container.get_attribute('href')
    links.append(link)
    


# In[16]:


for price_container in price_containers:
    price=price_container.text
    prices.append(price)
    


# In[17]:


len(product_descriptions)


# In[18]:


prices


# In[19]:


len(prices)


# In[20]:


len(links)


# In[21]:


my_dict={'product_description':product_descriptions,'price':prices,'link':links}


# In[22]:


#price_in_amazon=pd.DataFrame(my_dict)

price_in_amazon= pd.DataFrame(my_dict)



# In[23]:


price_in_amazon.to_csv('INDIA_amazon.csv') 


# In[24]:


#browser.quit()


# In[25]:


#try:
    #browser.find_elements(by='xpath',value='//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator" and not (@aria-disabled)]')
    
#except No_next_page_element:


# In[26]:


website_amazon_USA="https://www.amazon.com/"


# In[ ]:





# In[27]:


browser.get(website_amazon_USA)


# In[28]:


#address_change=browser.find_element(by='xpath',value='//span[@class="a-button a-spacing-top-base a-button-base glow-toaster-button glow-toaster-button-dismiss"]')


# In[29]:


#address_change.click()


# In[30]:


search_item="lenovo legion 5"


# In[31]:


search_bar=browser.find_element(by='id',value="twotabsearchtextbox")


# In[32]:


search_bar.send_keys(search_item)


# In[33]:


search_button=browser.find_element(by='id',value="twotabsearchtextbox").submit()


# In[34]:


containers=browser.find_elements(by='xpath',value='//span[@class="a-size-medium a-color-base a-text-normal"]')


# In[35]:


#//div[@class="sg-col-inner"]//h2//span


# In[36]:


#//div[@class="sg-col-inner"]//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]


# In[37]:


time.sleep(5)


# In[38]:


link_containers=browser.find_elements(by='xpath',value='//div[@class="a-section a-spacing-small a-spacing-top-small"]//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')


# In[39]:


price_containers=browser.find_elements(by='xpath',value='//div[@class="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right"]//span[@class="a-price"]')


# In[40]:


product_descriptions_US=[]
links_US=[]
prices_US=[]


# In[41]:


for container in containers:
    product_description=container.text
    product_descriptions_US.append(product_description)
    


# In[42]:


for link_container in link_containers:
    link=link_container.get_attribute('href')
    links_US.append(link)
    


# In[43]:


for price_container in price_containers:
    price=price_container.text
    prices_US.append(price)


# In[44]:


len(product_descriptions_US)


# In[45]:


len(links_US)


# In[46]:


len(prices_US)


# In[47]:



my_dict_2={'product_description':product_descriptions_US,'price':prices_US ,'link':links_US}


# In[48]:


price_in_amazon_US= pd.DataFrame(my_dict_2)


# In[49]:


price_in_amazon_US.to_csv('US_amazon.csv') 


# In[50]:


browser.quit()


# In[51]:


amazon_us_df=pd.read_csv('US_amazon.csv')


# In[52]:


amazon_us_df


# In[53]:


amazon_us_df['price']=amazon_us_df['price'].str.replace('$','')


# In[54]:


amazon_us_df['price']=amazon_us_df['price'].str.replace('\n','.')


# In[55]:


amazon_us_df['price']=amazon_us_df['price'].str.replace(',','').astype(float)


# In[56]:


currency_exchange_website='https://www.google.com/search?q=+usd+to+inr&sxsrf=ALiCzsb3HS7JjXEPliF4CKUG-BJ8LluF5g%3A1662705893287&ei=5eAaY6qREfrD4-EPvaKymAc&ved=0ahUKEwjql4qRjof6AhX64TgGHT2RDHMQ4dUDCA4&uact=5&oq=+usd+to+inr&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyCggAEIAEEIcCEBQyBQgAEJECMgUIABCABDIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQzoECAAQQ0oECEEYAEoECEYYAFCcBli7C2DlD2gCcAF4AIABd4gB6wGSAQMwLjKYAQCgAQHIAQrAAQE&sclient=gws-wiz'


# In[57]:


options=Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-site-isolation-trials")

path="M:\chromedriver.exe"
service=Service(executable_path=path)
browser=webdriver.Chrome(service=service,options=options)


# In[58]:


browser.get(currency_exchange_website)

    


# In[59]:


current_exchange_rate= browser.find_element(by='xpath',value='//span[@class="DFlfde SwHCTb"]').text


# In[60]:


current_exchange_rate=float(current_exchange_rate)


# In[61]:


current_exchange_rate


# In[62]:


browser.quit()


# In[63]:


amazon_us_df['price']=amazon_us_df['price']*current_exchange_rate


# In[64]:


amazon_us_df


# In[65]:


min_price_US_row=amazon_us_df[amazon_us_df.price==amazon_us_df.price.min()]


# In[66]:


min_price_US_row


# In[67]:


#type(amazon_us_df)


# In[68]:


#amazon_us_df.dtypes


# In[69]:


amazon_us_df['price'].min()


# In[70]:


min_price_USA=amazon_us_df['price'].min()


# In[71]:


amazon_us_df


# In[72]:


amazon_in_df=pd.read_csv('INDIA_amazon.csv')


# In[73]:


amazon_in_df['price']=amazon_in_df['price'].str.replace(',','').astype(float)


# In[74]:


min_price_IN_row=amazon_in_df[amazon_in_df.price==amazon_in_df.price.min()]


# In[75]:


min_price_INDIA=amazon_in_df['price'].min()


# In[91]:



if min_price_INDIA<min_price_USA:
    min_price_IN_row.to_csv("CHEAPEST PRICE_INDIA.csv")
else:
    min_price_US_row.to_csv("CHEAPEST PRICE_USA.csv")
        
        
        
        
        


# In[79]:


type(min_price_IN_row)


# In[83]:


min_price_INDIA<min_price_USA


# In[84]:


min_price_INDIA>min_price_USA


# In[ ]:





# In[ ]:





# In[ ]:




