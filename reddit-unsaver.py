#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
from IPython.display import clear_output


# In[2]:


from creds import username,password


# In[3]:


driver = webdriver.Chrome()
driver.get("https://redditmanager.com")
time.sleep(20)


# In[4]:


loginbutton = driver.find_element_by_class_name("login-btn")
loginbutton.click()
time.sleep(20)


# In[5]:


usernameentrybox = driver.find_element_by_id("user_login")
usernameentrybox.send_keys(username)


# In[6]:


passbox = driver.find_element_by_id("passwd_login")
passbox.send_keys(password)


# In[6]:


login = driver.find_element_by_class_name("button")
login.click()
time.sleep(10)


# In[7]:


allow = driver.find_element_by_name("authorize")
allow.click()
time.sleep(69)


# In[8]:


recent = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[3]")
recent.click()


# In[16]:


posts = driver.find_elements_by_xpath('//div[@class="item sub-item"]')
i=0
for post in posts:
    titlepart = driver.find_element_by_class_name("title")
    titlepart.click()
    time.sleep(1)
    deletebutton = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[3]/i')
    deletebutton.click()
    time.sleep(1)
    confirm = driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button')
    confirm.click()
    time.sleep(1)
    ok = driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button')
    ok.click()
    time.sleep(1)
    recent = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]')
    recent.click()
    clear_output(wait=True)
    i+=1
    display(i)

