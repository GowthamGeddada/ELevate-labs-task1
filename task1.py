#!/usr/bin/env python
# coding: utf-8

# # loading dataset

# In[1]:


import pandas as pd
df = pd.read_csv(r"D:\elevate labs\task1\marketing_campaign.csv",sep="\t")
df


# # handling missing values

# In[2]:


print(df.isnull().sum())


# # 

# In[3]:


df = df.dropna()
df


# In[4]:


print(df.isnull().sum())


# In[5]:


df.shape


# # handling duplicates

# In[6]:


df = df.drop_duplicates()


# In[7]:


df.shape


# # standardising text

# In[8]:


text_cols = df.select_dtypes(include=["object"]).columns.tolist()
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()


if "marital_status" in df.columns:
    df["marital_status"] = df["marital_status"].replace({
        "Single": "Single",
        "Together": "Married",
        "Married": "Married",
        "Divorced": "Divorced",
        "Widow": "Widowed",
        "Alone": "Single",
        "Absurd": "Other",
        "Yo-lo": "Other"
    })

if "education" in df.columns:
    df["education"] = df["education"].replace({
        "2n cycle": "Secondary",
        "Basic": "Basic",
        "Graduation": "Graduate",
        "Master": "Master",
        "PhD": "PhD"
    })


# # checking date formats

# In[9]:


df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], format="%d-%m-%Y", errors="coerce")


# # rename column headers 

# In[10]:


df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


# # fixing data types

# In[11]:


df["year_birth"] = df["year_birth"].astype(int)
df["id"] = df["id"].astype(int)
df["income"] = df["income"].astype(int)
df["teenhome"] = df["teenhome"].astype(int)
df["kidhome"] = df["kidhome"].astype(int)


# # cleaned data set

# In[12]:


df


# In[13]:


df.to_csv("D:/elevate labS/task1/cleaned_customer_personality.csv", index=False)


# In[ ]:




