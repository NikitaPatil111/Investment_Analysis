#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


df=pd.read_csv('C:/Users/nikit/OneDrive/Desktop/Data Analytics Material/Full project/Investment_data.csv', encoding='unicode_escape')


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


#drop a single column
df.drop(['Purpose'],axis=1,inplace=True)


# In[8]:


df.shape


# In[9]:


#check null values 
pd.isnull(df).sum()


# In[10]:


#droping null values 
df.dropna(inplace=True)


# In[11]:


df['age'].dtypes


# In[12]:


df['gender'].dtypes


# In[14]:


#chnage data type
df['gender'] = df['gender'].astype('string')


# In[15]:


df['gender'].dtypes


# In[16]:


df.columns


# In[17]:


#rename columns
df.rename(columns={'Expect':'Expected returns'})


# In[18]:


df.describe()


# In[20]:


#use describe method for specific column
df[['gender','Mutual_Funds','Stock_Marktet']].describe()


# In[22]:


#use describe method for specific column
df[['Stock_Marktet']].describe()


# In[23]:


#ploting a bar chart for Gender and it's count

ax=sns.countplot(x='gender',data=df)


# In[27]:


ax = sns.countplot(data=df, x='age', hue='gender')  

for bars in ax.containers:
    ax.bars_labels(bars)


# In[41]:


# Boxplot for numerical columns to detect outliers
plt.figure(figsize=(10,6))
sns.boxplot(data=df[['Mutual_Funds', 'Gold', 'Stock_Marktet']])
plt.show()


# In[51]:


df=pd.read_csv('C:/Users/nikit/OneDrive/Desktop/Data Analytics Material/Full project/Investment_data.csv', encoding='unicode_escape')


# In[55]:


import pandas as pd

# Assuming df is your DataFrame, you can drop the specified columns
df = df.drop(columns=['Purpose', 'Reason_Mutual'])


# In[58]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
Investment_data = pd.read_csv('C:/Users/nikit/OneDrive/Desktop/Data Analytics Material/Full project/Investment_data.csv')

# Now plot the age distribution
plt.figure(figsize=(6, 4))
sns.histplot(Investment_data['age'], bins=10, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[61]:


# Investment preferences by gender
investment_columns = ['Mutual_Funds', 'Equity_Market', 'Debentures', 'Government_Bonds', 'Fixed_Deposits', 'PPF', 'Gold']
Investment_data.groupby('gender')[investment_columns].mean().plot(kind='bar', figsize=(10, 6))
plt.title('Average Investment Preferences by Gender')
plt.ylabel('Average Investment Score')
plt.xlabel('Gender')
plt.legend(title='Investment Types')
plt.show()


# In[62]:


# Popular investment avenues
popular_avenues = Investment_data['Avenue'].value_counts()
print("Most Popular Investment Avenues:\n", popular_avenues)


# In[65]:


# Fill missing values
investment_data_cleaned = Investment_data.fillna({
    'gender': 'Unknown',  # Fill missing genders with 'Unknown'
    'age': Investment_data['age'].mean(),  # Fill missing ages with the mean
    'Investment_Avenues': 'No',  # Assume 'No' for missing investment avenues
    'Expect': 'Unknown',  # Placeholder for missing expectations
    'Source': 'Unknown'  # Placeholder for missing sources
})


# In[63]:


# Savings objectives
savings_objectives = Investment_data['What are your savings objectives?'].value_counts()
print("Savings Objectives Distribution:\n", savings_objectives)


# In[64]:


# Verify missing values are resolved
print("Missing Values After Cleaning:\n", Investment_data.isnull().sum())


# In[66]:


#Save the Cleaned Data
cleaned_file_path = 'Cleaned_Investment_Data.csv'
investment_data_cleaned.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")


# Saves the cleaned dataset as Cleaned_Investment_Data.csv for SQL and Power BI.
