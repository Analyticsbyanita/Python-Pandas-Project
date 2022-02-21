#!/usr/bin/env python
# coding: utf-8

# In[82]:


### Q1. What is  the overall sales trend?
### Q2. Which are the Top 10 products by sales?
### Q3. Which are the Most Selling Products?
### Q4. Which is the most prefered Ship Mode?
### Q5. Which are the Most Profitable Category and Sub-Category?


# ## IMPORT LIBRARIES

# In[83]:


import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# ## FOR FIRST 5 ROWS

# In[84]:


df = pd.read_excel(r"C:\Users\anita\Documents\Data analysis\Sales-Analysis-master\Sales-Analysis-master\superstore_sales.xlsx")

df.head()


# ## LAST 5 ROWS

# In[85]:


df.tail()


# In[86]:


df.shape


# In[87]:


df.columns


# In[88]:


df.info()


# In[89]:


df.isnull().sum()


# In[90]:


df.describe()


# ## EXPLORATORY DATA ANALYSIS

# ## What is  the overall sales trend?

# In[91]:


df['order_date'].min()


# In[92]:


df['order_date'].max()


# In[93]:


df["month_year"] = df["order_date"].apply(lambda x: x.strftime("%Y-%m"))


# In[94]:


# Getting Month Year from dataset
df["month_year"]


# In[95]:


# Grouping Month Year
df_trend = df.groupby("month_year").sum()["sales"].reset_index()


# In[96]:


# Setting Fthe Figure Sizes
plt.figure(figsize = (15, 6))
plt.plot(df_trend["month_year"], df_trend["sales"], color = "#b80045")
plt.xticks(rotation='vertical', size = 8)
plot.show()


# ## Which are the Top 10 products by sales?

# In[ ]:


# Group Product name column
prod_sales = pd.DataFrame(df.groupby('product_name').sum()["sales"])


# In[ ]:


prod_sales.sort_values("sales", ascending=False)


# In[ ]:


# Top 10 by product by sales
prod_sales[:10]


# <h4> Which are the Highest Grossing Products?

# In[ ]:


# Grouping product name
most_sell_prod = pd.DataFrame(df.groupby("product_name").sum()["quantity"])


# In[ ]:


# Sorting most_sell_products
most_sell_prod = most_sell_prod.sort_values('quantity',ascending=False)


# In[97]:


most_sell_prod[:10]


# ## Which is the most prefered Ship Mode

# In[104]:


plt.figure(figsize = (10,8.5))

sns.countplot(df["ship_mode"])

plt.show()


# In[106]:


##Which are the Most Profitable Category and Sub-Category?


# In[110]:


cat_subcat_profit = pd.DataFrame(df.groupby(['category', 'sub_category']).sum()['profit'])


# In[113]:


cat_subcat_profit.sort_values(['category', 'profit'], ascending = False)

