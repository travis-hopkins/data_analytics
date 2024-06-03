#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('cars_by_popular_city.csv')


# In[3]:


df.shape


# In[4]:


df.columns


# In[5]:


df['Location'].value_counts()


# In[6]:


df['Brand'].value_counts()


# In[7]:


df['Status'].value_counts()


# In[ ]:




