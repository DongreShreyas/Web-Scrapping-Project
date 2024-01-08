#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


get_ipython().system('pip install requests')


# In[4]:


get_ipython().system('pip install beautifulsoup4')


# In[5]:


get_ipython().system('pip3 install beautifulsoup4')


# In[22]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name=[]
Prices=[]
Description=[]
Reviews=[]


url ="https://www.flipkart.com/search?q=mobile+under+20000rs&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_12_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile+under+20000rs%7CMobiles&requestId=c763fe4c-7a03-4a30-98af-5b4b2dc7c31c&as-searchtext=mobile%20under"+str(1)
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text,"lxml")

box=soup.find("div",class_="_1YokD2 _3Mn1Gg")

names = box.find_all("div",class_ ="_4rR01T")


    name = i.text
    Product_name.append(name)
print(len(Product_name)) 
print(Product_name)




prices = box.find_all("div",class_="_30jeq3 _1_WHN1")


    name = i.text
    Prices.append(name)
print(len(Prices)) 
print(Prices)


desc = box.find_all("ul",class_="_1xgFaf")


    name = i.text
    Description.append(name)
print(len( Description)) 
print( Description)


reviews= box.find_all("div",class_="_3LWZlK")


    name = i.text
    Reviews.append(name)
print(len( Reviews)) 
print( Reviews)



# In[ ]:




