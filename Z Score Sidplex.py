#!/usr/bin/env python
# coding: utf-8

# # Z-Score

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import zscore, percentileofscore


# In[2]:


df=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\weight-height.csv")
df


# In[7]:


df_male=df[df['Gender']=='Male'].copy()
df_female=df[df['Gender']=='Male'].copy()


# In[8]:


df_male['zscore_male_height']=zscore(df_male['Height'])
df_male['zscore_male_weight']=zscore(df_male['Weight'])


# In[9]:


df_female['zscore_female_height']=zscore(df_female['Height'])
df_female['zscore_female_weight']=zscore(df_female['Weight'])


# In[10]:


print(df_female)


# In[11]:


print(df_male)


# In[12]:


frame=[df_male,df_female]
result =pd.concat(frame)
df=result
df


# # lets try with other dataset 

# In[15]:


df=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\Australian_Student_PerformanceData (ASPD24).csv")
df


# In[16]:


df['Final Exam Scores']


# In[17]:


pi_mean=df['Final Exam Scores'].mean()
pi_std=df['Final Exam Scores'].std()
print(pi_mean)
print(pi_std)


# In[18]:


df['pi_percentile']=df['Final Exam Scores'].rank(pct=True)*100
#rank(pct=True): Ranks the values as a percentage (between 0 and 1).
#Multiplying by 100 gives percentile values from 0 to 100.


# In[19]:


df['pi_zscore']=zscore(df['Final Exam Scores'])
df


# In[20]:


#lets try one more
df=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\Student_Performance.csv")
df


# In[21]:


pi_mean=df['Performance Index'].mean()
pi_std=df['Performance Index'].std()


# In[22]:


df['pi_percentile']=df['Performance Index'].rank(pct=True)*100


# In[23]:


#display mean and SD
print(f"Mean of Performance Index:{pi_mean:.2f}")
print(f"SD of Performance Index:{pi_std:.2f}")


# In[24]:


df['pi_zscore']=zscore(df['Performance Index'])


# In[25]:


print(df.head())


# In[26]:


#save the modified DF to CSV file
df.to_csv(r'E:\MY CDAC NOTES\new\Analytics\Student-Performance-with-z-scores-and-percentiles.csv',index=False)


# In[ ]:




