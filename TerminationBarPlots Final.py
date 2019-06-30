#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import os

data = pd.read_excel("data.xlsx",sheet_name= None)
Merit_df = pd.DataFrame(data["Sheet1"])
SMSF_df = pd.DataFrame(data["Sheet2"])

Merit_df["Diff Notice & Term (Months)"] = (Merit_df["Termination Date"] - Merit_df["Notice Date"])/np.timedelta64(1,'M')
Merit_df["Diff Appoint & Notice (Months)"] = (Merit_df["Notice Date"] - Merit_df["Date Appointed"])/np.timedelta64(1,'M')
Merit_df = Merit_df.sort_values(by =['Notice Date'])
Merit_df.head()


# In[4]:


NoticeDate_df= Merit_df.groupby(Merit_df["Notice Date"].dt.strftime("%b %Y"))["Diff Notice & Term (Months)"].mean().reset_index()
print(NoticeDate_df)


# In[5]:


NoticeDate_df["Notice Date"] = NoticeDate_df["Notice Date"].apply(lambda x: datetime.datetime.strptime(x,"%b %Y"))
NoticeDate_df.head()


# In[6]:


NoticeDate_df = NoticeDate_df.sort_values(by=["Notice Date"], ascending=True)


# In[7]:


NoticeDate_df 


# In[8]:


NoticeDate_df["Notice Date"] = NoticeDate_df["Notice Date"].apply(lambda x: x.strftime("%b %Y"))


# In[9]:


NoticeDate_df.drop(labels=1)


# In[10]:


NoticeDate_df.plot.bar(x="Notice Date", y="Diff Notice & Term (Months)", figsize=(10,10))
plt.title('Bar chart of Time Taken to Terminate from Notice Date')
plt.xlabel('Date')
plt.ylabel('Number of Months')
plt.savefig('Notice_Terminate_Chart.png', bbox="tight" )


# In[11]:


DateAppoint_df = Merit_df.groupby(Merit_df["Notice Date"].dt.strftime("%b %Y"))["Diff Appoint & Notice (Months)"].mean().reset_index()
DateAppoint_df["Notice Date"] = DateAppoint_df["Notice Date"].apply(lambda x: datetime.datetime.strptime(x,"%b %Y"))
DateAppoint_df = DateAppoint_df.sort_values(by=["Notice Date"], ascending= True)
DateAppoint_df


# In[12]:


DateAppoint_df["Notice Date"] = DateAppoint_df["Notice Date"].apply(lambda x: x.strftime("%b %Y"))


# In[13]:


DateAppoint_df.plot.bar(x="Notice Date", y="Diff Appoint & Notice (Months)", color="orange", figsize=(18,10))
plt.title('Bar chart of Time Taken from Start Date to Notice Date')
plt.xlabel('Date')
plt.ylabel('Number of Months')
plt.savefig("Start_Notice_Chart.png",bbox="tight")


# In[14]:


bar1 = DateAppoint_df["Diff Appoint & Notice (Months)"]
bar2 = NoticeDate_df["Diff Notice & Term (Months)"]


# In[15]:


bar1= list()
bar2= list()
for value in DateAppoint_df["Diff Appoint & Notice (Months)"]:
    bar1.append(value)
for value in NoticeDate_df["Diff Notice & Term (Months)"]:
    bar2.append(value)


# In[16]:


date=list()
for dates in DateAppoint_df["Notice Date"]:
    date.append(dates)


# In[55]:


plt.figure(figsize=(16,10))
barWidth=1.5
x_index=[0,2,4,6,8,10,12]
y_index=[0,14,21,28,35,42] 
plt.bar(index, bar1, color='skyblue', edgecolor='white', width=barWidth)
plt.bar(index, bar2, bottom=bar1, color="sandybrown", edgecolor='white', width=barWidth)
plt.xlabel('Date', fontsize="18", fontweight="bold")
plt.xticks(x_index, date,fontsize="14", rotation=0)
plt.ylabel('Months', fontsize="18", fontweight="bold")
plt.yticks([0,6,12,18,24,30,36],fontsize="14")
axes = plt.gca()
axes.set_ylim([0,36])
plt.title('Bar chart of Time Taken from Start Date to Terminate Date', fontsize="16" )
plt.legend(["Start to Notice Date", "Notice to Terminate Date"],loc=2, fontsize="large")

plt.savefig("Final_Chart.png",bbox="tight")


# In[ ]:





# In[ ]:




