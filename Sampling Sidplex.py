#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[7]:


df=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\weight-height.csv")
df.head()


# In[10]:


rows=len(df)
rows


# # simple Sampling

# In[12]:


sample_fraction = 0.1


# In[14]:


sample_df = df.sample(frac=sample_fraction, random_state=42)
# - frac=: number of samples to draw
# - random_state=42: fixed seed for reproducibility (same results every time)


# In[15]:


sample_df.head()


# In[16]:


len(sample_df)


# # Systamatic Sampling

# In[18]:


every_7th_df = df.iloc[6::7]  # Index 6 is the 7th row (0-based indexing)


# In[19]:


every_7th_df


# # Stratified Sampling

# In[21]:


Male_df=df[df["Gender"]=="Male"]
len(Male_df)


# In[22]:


Female_df=df[df["Gender"]=="Female"]
len(Female_df)


# In[39]:


#problem Statement 80%males and 20%females
sample_fraction_male = 0.8
sample_df_male = Male_df.sample(frac=sample_fraction_male, random_state=42)


# In[40]:


len(sample_df_male)


# In[41]:


sample_fraction_male = 0.2
sample_df_female = Female_df.sample(frac=sample_fraction_male, random_state=42)


# In[42]:


len(sample_df_female)


# In[43]:


strat_sample=pd.concat([sample_df_male,sample_df_female])
strat_sample.shape
strat_sample


# # cluster sampling 

# In[ ]:




