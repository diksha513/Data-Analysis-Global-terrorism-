#!/usr/bin/env python
# coding: utf-8

# # Task         : Exploratory Data Analysis (Global Terrorism) 
# # Category     : Data science & Business Analytics
# # Performed by : Diksha P Gadataranavar
# # Organization : The Sparks Foundation

# In[131]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# ## Reading the dataset of terrorism 

# In[135]:


new_data=pd.read_csv(r"C:\Users\diksha\Documents\Newprojects\terrorist.csv",encoding="Latin1")


# In[136]:


new_data.head()


# In[137]:


new_data.shape


# In[138]:


new_data.rename(columns={'eventid':'Event_ID','iyear':'Year','country':'No.of_attack','region':'No.of_region','imonth':'Month', 'iday':'Day', 'country_txt':'Country', 'region_txt':'Region', 'provstate':'State', 'city':'City',
                   'attacktype1_txt':'Attack_Type', 'targtype1_txt':'Target_Type', 'motive':'Motive', 'weaptype1_txt':'Weapon_Type',
                   'weapdetail':'Weapon_Details', 'nkill':'Kill', 'nwound':'Injured', 'summary':'Summary'}, inplace=True)


# ## Countries under High Terrorism attack

# In[181]:


print("Countries under High Terrorism attack")
new_data['Country'].value_counts().head()


# In[183]:


plt.figure(figsize=(15,6))
sns.barplot(new_data['Country'].value_counts()[:10].index, new_data['Country'].value_counts()[:10].values)
plt.xlabel(' Countries under Terrorism', fontsize=15)
plt.ylabel('Terrorism attack Count', fontsize=15)
plt.title(' Countries under High Terrorism attack ', fontsize=35)
plt.xticks(rotation=90)
plt.show()


# In[125]:


print("Country with less terrorism ")
new_data['Country'].value_counts().tail()


# ## Here we get that countries like Iraq ,Pakistan ,Afghanistan ,India ,Colombia have most terrorism attacks  

# In[180]:


#line graph for country vs kill
plt.figure(figsize=(15,6))
sns.barplot(new_data['Country'].value_counts()[:10].index, new_data['Kill'].value_counts()[:10].values)
plt.xlabel(' Countries under Terrorism ', fontsize=15)
plt.ylabel('Kill range ', fontsize=15)
plt.title(' kills due to terrorism attacks ', fontsize=35)
plt.show()


# In[148]:


print('Number of pepople Killed and Injured per year')
year1 = new_data.groupby(['Year'])['Kill', 'Injured'].sum()
year1.head(8)


# In[149]:


print('Number of people Killed and Injured per year')
year2 = new_data.groupby(['Year'])['Kill', 'Injured'].sum()
year2.tail(10)


# In[170]:


plt.figure(figsize=(15,6))
sns.barplot("Year","Kill",data=new_data)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Kills', fontsize=15)
plt.title('Number of people Killed and Injured per year ', fontsize=39)
plt.xticks(rotation=90)
plt.show()


# In[185]:


plt.figure(figsize=(15,6))
sns.countplot('Year', data=new_data)
plt.xlabel('Year ',fontsize=15)
plt.ylabel('Terrorism attack Count',fontsize=15)
plt.title('Count of terrorism attack per Year ', fontsize=25)
plt.xticks(rotation=90)
plt.show()


# ## Count of terrorism attacks per year has been seen increasing

# In[67]:


attack_type = new_data.groupby(['Country'])['Attack_Type', 'Weapon_Type'].max()
attack_type.head(10)


# In[153]:


print("Attacking Type used by Terrorist")
new_data['Attack_Type'].value_counts()


# In[171]:


plt.figure(figsize=(15,6))
sns.barplot(new_data['Attack_Type'].value_counts()[:10].index, new_data['Attack_Type'].value_counts()[:10].values)
plt.xlabel('Attack type used by Terrorist',fontsize=15)
plt.ylabel('Attack  Count',fontsize=15)
plt.title(' Attacking Type used by Terrorist ', fontsize=30)
plt.xticks(rotation=90)
plt.show()


# In[154]:


print("Weapon types used for attacking purpose")

new_data['Weapon_Type'].value_counts()


# In[178]:


plt.figure(figsize=(15,6))
sns.barplot(new_data['Weapon_Type'].value_counts()[:10].index, new_data['Weapon_Type'].value_counts()[:10].values)
plt.xlabel('Weapons used by Terrorists', fontsize=15)
plt.ylabel('Weapons Count' ,fontsize=15)
plt.title(' Weapons used by Terrorists ', fontsize=30)
plt.xticks(rotation=90)
plt.show()


# ## Attack type is mostly Bombing/Explosive which creates high death rate and certain other illeffects

# In[156]:


print("Region which is used for attacking purpose")

region = new_data['Region'].value_counts()
region.head()


# In[158]:



plt.figure(figsize=(15,6))
sns.countplot('Region', data=new_data)
plt.xlabel('Region of Terrorism attacks', fontsize=15)
plt.ylabel('Region attacks Count', fontsize=15)
plt.title('Region that has Maximun Terrorist Attacks ', fontsize=30)
plt.xticks(rotation=90)
plt.show()


# ## Middle East ,North Africa ,South Asia ,South America are the regions under maximum attacks   

# In[88]:


#city which is hot zone
city = new_data['City'].value_counts()
city.head()


# In[184]:



plt.figure(figsize=(15,6))
sns.barplot(new_data['City'].value_counts()[:15].index, new_data['City'].value_counts()[:15].values)
plt.xlabel('Cities ', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.title('Cities with most attacks ', fontsize=36)
plt.xticks(rotation=90)
plt.show()


# ## Cities like baghdad,karachi,Lima have high number of attacks 

# # Thankyou
