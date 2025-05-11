#!/usr/bin/env python
# coding: utf-8

# # Conditional Probaility

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


df_2015=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\marathon_results_2015.csv")
df_2016=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\marathon_results_2016.csv")
df_2017=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\marathon_results_2017.csv")


# In[5]:


df=pd.concat([df_2015,df_2016,df_2017])
df.head()


# In[6]:


#powerfull line to split the column Official Time into Hours Min and Sec and expand=True means split data into different columns 
df[['Hours','Minutes','Seconds']]=df['Official Time'].str.split(':',expand=True)


# In[7]:


#forcefully converting the column values into integer
df['Hours']=df['Hours'].astype(int)
df['Minutes']=df['Minutes'].astype(int)
df['Seconds']=df['Seconds'].astype(int)
df['finish_time_in_seconds']=df['Hours']*3600+df['Minutes']*60+df['Seconds']


# In[8]:


#we are doing this for the pace columns
df[['Hours','Minutes','Seconds']]=df['Pace'].str.split(':',expand=True)


# In[9]:


#forcefully converting the column values into integer
df['Hours']=df['Hours'].astype(int)
df['Minutes']=df['Minutes'].astype(int)
df['Seconds']=df['Seconds'].astype(int)
df['Pace_in_seconds']=df['Hours']*3600+df['Minutes']*60+df['Seconds']


# In[11]:


condition_A=df['finish_time_in_seconds']<=3*60*60 # finish within 3 hours
condition_B=df['Pace_in_seconds']<8*60 #pace less than 8 min per kilom


# In[12]:


#calculating the probabilites
P_B=len(df[condition_B])/len(df)
P_A_and_B=len(df[condition_A & condition_B]) # this is derived by shifting the formula
P_A_given_B=P_A_and_B/P_B
print(f"P(A|B))={P_A_given_B:.4f}")


# In[ ]:




