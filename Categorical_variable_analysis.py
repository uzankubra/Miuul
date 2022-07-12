#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns 


# In[2]:


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=sns.load_dataset("titanic")


# In[3]:


df.head()


# In[4]:


df["sex"].value_counts()


# In[5]:


df["sex"].nunique()


# In[6]:


df["sex"].unique()


# In[7]:


cat_cols= [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]


# In[14]:


num_but_cat= [col for col in df.columns if df[col].nunique()<10 and df[col].dtypes in ["int", "float"]]


# In[15]:


cat_but_car=[col for col in df.columns if df[col].nunique()>20 and str(df[col].dtypes) in ["category", "object"]]


# In[16]:


cat_but_car


# In[17]:


cat_cols=[col for col in cat_cols if col not in cat_but_car]


# In[18]:


cat_cols= cat_cols + num_but_cat


# In[19]:


cat_cols


# In[20]:


df[cat_cols]


# In[22]:


df[cat_cols].nunique()


# In[23]:


100 * df["survived"].value_counts() / len(df)


# In[36]:


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                       "Ratio": 100* dataframe[col_name].value_counts() /len(dataframe)}))
    print("###########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block= True)


# In[37]:


cat_summary(df, "sex")


# In[38]:


for col in cat_cols:
    cat_summary(df, col)


# In[39]:


cat_summary(df, "sex", plot= True)


# In[41]:


for col in cat_cols:
    if df[col].dtypes =="bool":   #bool veri tipine geldiginde hata veriyor 
        print("hata almamak icin fonksiyon calistirilmiyor cunku veri tipi bool ")
    else:
        cat_summary(df, col, plot=True) 


# In[43]:


# ornek olarak hata aldigim bool deger adult_male
df["adult_male"].astype(int)


# In[44]:


#fonksiyonu su sekilde yazarsak bool dahil tum veri tiplerinde calisir.
for col in cat_cols:
    if df[col].dtypes =="bool":   
        df[col]=df[col].astype(int)
        cat_summary(df, col, plot=True) 
    else:
        cat_summary(df, col, plot=True) 


# In[45]:


df[["age", "fare"]].describe().T


# In[46]:


num_cols= [col for col in df.columns if col not in cat_cols]


# In[48]:


def num_summary(dataframe, numerical_col):
    quantiles=[0.05, 0.10, 0.20, 0.30 , 0.40 ,0.50 , 0.60 ,0.70, 0.80, 0.90]
    print(dataframe[numerical_col].describe(quantiles).T)


# In[49]:


for col in num_cols:
    num_summary(df,col)


# In[50]:


def num_summary(dataframe, numerical_col, plot= False):
    quantiles=[0.05, 0.10, 0.20, 0.30 , 0.40 ,0.50 , 0.60 ,0.70, 0.80, 0.90]
    print(dataframe[numerical_col].describe(quantiles).T)
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)
        


# In[51]:


for col in num_cols:
    num_summary(df,col, plot=True)


# In[ ]:




