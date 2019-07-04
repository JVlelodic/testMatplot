#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import os

data = pd.read_excel("Final_termination.xlsx",sheet_name= None)
Merit_df = pd.DataFrame(data["SMSF"])


Merit_df["Diff Notice & Term (Months)"] = (Merit_df["Termination Date"] - Merit_df["Notice Date"])/np.timedelta64(1,'M')
Merit_df["Diff Appoint & Notice (Months)"] = (Merit_df["Notice Date"] - Merit_df["Date Appointed"])/np.timedelta64(1,'M')
Merit_df = Merit_df.sort_values(by =['Notice Date'])
Merit_df.head()


# In[2]:


NoticeDate_df= Merit_df.groupby(Merit_df["Notice Date"].dt.strftime("%b %Y"))["Diff Notice & Term (Months)"].mean().reset_index()
NoticeDate_df.head()


# In[3]:


NoticeDate_df["Notice Date"] = NoticeDate_df["Notice Date"].apply(lambda x: datetime.datetime.strptime(x,"%b %Y"))
NoticeDate_df.head()


# In[4]:


NoticeDate_df = NoticeDate_df.sort_values(by=["Notice Date"], ascending=True)


# In[5]:


NoticeDate_df 


# In[6]:


NoticeDate_df["Notice Date"] = NoticeDate_df["Notice Date"].apply(lambda x: x.strftime("%b %Y"))


# In[7]:


NoticeDate_df.drop(labels=1)


# In[8]:


NoticeDate_df.plot.bar(x="Notice Date", y="Diff Notice & Term (Months)", figsize=(10,10))
plt.title('Bar chart of Time Taken to Terminate from Notice Date')
plt.xlabel('Date')
plt.ylabel('Number of Months')


# In[9]:


DateAppoint_df = Merit_df.groupby(Merit_df["Notice Date"].dt.strftime("%b %Y"))["Diff Appoint & Notice (Months)"].mean().reset_index()
DateAppoint_df["Notice Date"] = DateAppoint_df["Notice Date"].apply(lambda x: datetime.datetime.strptime(x,"%b %Y"))
DateAppoint_df = DateAppoint_df.sort_values(by=["Notice Date"], ascending= True)
DateAppoint_df


# In[10]:


DateAppoint_df["Notice Date"] = DateAppoint_df["Notice Date"].apply(lambda x: x.strftime("%b %Y"))


# In[11]:


DateAppoint_df.plot.bar(x="Notice Date", y="Diff Appoint & Notice (Months)", color="orange", figsize=(18,10))
plt.title('Bar chart of Time Taken from Start Date to Notice Date')
plt.xlabel('Date')
plt.ylabel('Number of Months')


# In[12]:


Count_df= Merit_df.groupby(Merit_df["Notice Date"].dt.strftime("%b %Y"))["Diff Notice & Term (Months)"].count().reset_index()
Count_df["Notice Date"] = Count_df["Notice Date"].apply(lambda x: datetime.datetime.strptime(x,"%b %Y"))
Count_df = Count_df.sort_values(by=["Notice Date"], ascending=True)
Count_df["Notice Date"] = Count_df["Notice Date"].apply(lambda x: x.strftime("%b %Y"))
Count_df.head()


# In[13]:


line = list()
for val in Count_df["Diff Notice & Term (Months)"]:
    line.append(val)
print(line)


# In[14]:


bar1= list()
bar2= list()
for value in DateAppoint_df["Diff Appoint & Notice (Months)"]:
    bar1.append(value)
for value in NoticeDate_df["Diff Notice & Term (Months)"]:
    bar2.append(value)


# In[15]:


date=list()
for dates in DateAppoint_df["Notice Date"]:
    date.append(dates)


# In[16]:


plt.figure(figsize=(18,10))
barWidth=1.5
x_index=[0,2,4,6,8]
y_index=[0,14,21,28,35,42] 
plt.bar(x_index, bar1, color='skyblue', edgecolor='white', width=barWidth)
plt.bar(x_index, bar2, bottom=bar1, color="sandybrown", edgecolor='white', width=barWidth)
plt.xlabel('Notice Date', fontsize="18", fontweight="bold")
plt.xticks(x_index, date,fontsize="14", rotation=0)
plt.ylabel('Months', fontsize="18", fontweight="bold")
plt.yticks([0,6,12,18,24,30,36],fontsize="14")
plt.legend(["Start to Notice Date", "Notice to Terminate Date"],loc=2, fontsize="large")

axes = plt.gca()
axes.set_ylim([0,36])
axes2 = axes.twinx()

axes2.set_ylabel('People', fontsize="18", fontweight="bold")  
axes2.plot(x_index, line , color= "black")
# for a,b in zip(x_index, line): 
#     plt.text(a, b, str(b), fontsize=14)
axes2.tick_params(axis='y', labelsize=14)
plt.legend(["Number of People"],loc=1, fontsize="large")


plt.title('Bar chart of Time Taken from Start Date to Terminate Date (SMSF)', fontsize="16" )
plt.savefig("SMSF_Chart.png",bbox="tight")


# In[ ]:





# In[ ]:




