#!/usr/bin/env python
# coding: utf-8

# # Shapiro wilk test

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


# In[2]:


data=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\tips.csv")
data


# In[3]:


total_bill_series=data['total_bill']


# In[4]:


#normality test with shapiro-wilk test
shaprio_test=stats.shapiro(total_bill_series)
print('Test statistic (W):',shaprio_test.statistic)
print("p-value:",shaprio_test.pvalue)


# In[5]:


alpha=0.05 # common significance level
if shaprio_test.pvalue > alpha:
    print("data is normally distributed")
else:
    print("data is not normally distributed")


# # QQ Plot 

# In[7]:


stats.probplot(total_bill_series,dist='norm',plot=plt)
plt.title("QQ plot of total bill")
plt.xlabel('theoretical quantiles (normal distribution)')
plt.ylabel('ordered values (total bill)')
plt.grid(True)
plt.show()


# # lets take another Example
# 

# In[8]:


data1=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\titanic.csv")
data1


# # Shapiro wilk test will not take null values so lets use Dropna()

# total_age_series=data1['age']
# total_age_series=total_age_series.dropna()

# In[10]:


shaprio_test1=stats.shapiro(total_age_series)
print('Test statistic (W):',shaprio_test1.statistic)
print("p-value:",shaprio_test1.pvalue)


# In[11]:


alpha=0.05 # common significance level
if shaprio_test1.pvalue > alpha:
    print("data is normally distributed")
else:
    print("data is not normally distributed")


# # QQ plot 

# In[12]:


stats.probplot(total_age_series,dist='norm',plot=plt)
plt.title("OO plot of total bill")
plt.xlabel('theoretical quantiles (normal distribution)')
plt.ylabel('ordered values (total bill)')
plt.grid(True)
plt.show()


# In[ ]:




