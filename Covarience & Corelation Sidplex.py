#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt


# In[47]:


df=pd.read_csv(r"E:\MY CDAC NOTES\new\Analytics\weight-height.csv")
df.head()


# In[48]:


Male_df=df[df["Gender"]=="Male"]


# In[49]:


Male_df.head()


# In[50]:


Female_df=df[df["Gender"]=="Female"]
Female_df.head()


# # Covariance

# In[51]:


Cov_Male=Male_df[["Height","Weight"]].cov()
print("the male covarriance is: ")
print(Cov_Male)


# In[52]:


Cov_Female=Female_df[['Height','Weight']].cov()
print("the female covarriance is: ")
print(Cov_Female)


# # co-relation

# In[57]:


Corr_Male=Male_df[["Height","Weight"]].corr()
print("the male co-relation is: ")
print(Corr_Male)


# In[58]:


Corr_Female=Female_df[["Height","Weight"]].corr()
print("the female co-relation is: ")
print(Corr_Female)


# In[59]:


#creating scatter plt with corr val
fig,axes = plt.subplots(1,3,figsize=(18,6))
# in figsize 1,3 means in one row plot 3 columns of the image
#axes=2 = third column -look down

#female data plt
axes[2].scatter(Corr_Female["Height"],Corr_Female["Weight"],color="blue",alpha=0.5) # alpha means thickness of the dot 
axes[2].set_title(f'Female Correlation: {Corr_Female.loc["Height","Weight"]:.2f}')
axes[2].set_xlabel("Height")
axes[2].set_ylabel("Weight")
axes[2].grid(True)# horizontal and verticle lines

plt.tight_layout()
plt.show()


# In[62]:


#creating scatter plt with corr val
fig,axes = plt.subplots(1,3,figsize=(18,6))
# in figsize 1,3 means in one row plot 3 columns of the image
#axes=2 = third column -look down

#female data plt
axes[2].scatter(Corr_Female["Height"],Corr_Female["Weight"],color="blue",alpha=0.5) # alpha means thickness of the dot 
axes[2].set_title(f'Female Correlation: {Corr_Female.loc["Height","Weight"]:.2f}')
axes[2].set_xlabel("Height")
axes[2].set_ylabel("Weight")
axes[2].grid(True)# horizontal and verticle lines

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




