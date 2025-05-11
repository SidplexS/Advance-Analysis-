#!/usr/bin/env python
# coding: utf-8

# # box plot
# 

# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cars = pd.read_csv(r"D:\AA\Datasets\cars2018.csv")
cars.head()


# In[29]:


np.quantile(cars['MPG'],[0.25,0.5,0.75])# to find all Quartiles in one go !!!, returns array!!!


# In[30]:


# Plot boxplot
plt.boxplot(cars['MPG'])
plt.title('Boxplot of MPG')
plt.xlabel('Car /Models')
plt.ylabel('Miles Per Gallon')
plt.show()


# In[31]:


q1 = np.quantile(cars['MPG'],0.25)# to find Q1 Quartile
q3 = np.quantile(cars['MPG'],0.75)# to find Q3 Quartile
iqr = q3 - q1 #to find inter quartile range
low = q1 - 1.5*iqr #lowest limit
upp = q3 + 1.5*iqr #hightest limit
low, upp # printing values 


# In[32]:


df_low = cars[cars['MPG']<low]['MPG']# values less than low are extracted in diff coloumn 
df_low.head()# no values !!!
df_low.shape# no values !!!


# In[45]:


df_upp = cars[cars['MPG']>upp]['MPG']
df_upp.head() #found some outliers in upper range


# In[46]:


df_upp.shape#total 19 but incl repetations


# In[35]:


len(df_upp.unique())


# In[36]:


#----------------------------------------------------------------------------------------------------------------------------


# In[37]:


# creating function for outlier
def outliers_s(df, coloumn):
    q1 = np.quantile(df[coloumn],0.25)
    q3 = np.quantile(df[coloumn],0.75)
    iqr = q3 - q1
    low = q1 - 1.5*iqr
    upp = q3 + 1.5*iqr
    df_low = df[df[coloumn]<low][coloumn].values
    df_upp = df[df[coloumn]>upp][coloumn].values
    return  df_low,df_upp


# In[38]:


outliers_s(cars,'MPG')#calling function 


# In[39]:


len(df_low.unique())


# In[40]:


len(df_upp.unique())


# In[41]:


# Plot boxplot with new values
plt.boxplot(cars['MPG'])
plt.title('Boxplot of MPG')
plt.xlabel('Car /Models')
plt.ylabel('Miles Per Gallon')
plt.show()


# In[42]:


#got the same results!!!!!!!


# In[ ]:




