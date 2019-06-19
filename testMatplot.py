import pandas as pd
import datetime
import numpy
import matplotlib.pyplot as plt
import os

data = pd.read_excel("data.xlsx",sheet_name= None)
Merit_df = pd.DataFrame(data["Sheet1"])
SMSF_df = pd.DataFrame(data["Sheet2"])

Merit_df["Diff Notice & Term (Days)"] = (Merit_df["Termination Date"] - Merit_df["Notice Date"]).apply(lambda x: x.days)
Merit_df["Diff Appoint & Notice (Days)"] = (Merit_df["Notice Date"] - Merit_df["Date Appointed"]).apply(lambda x: x.days)
Merit_df = Merit_df.sort_values(by =['Notice Date'])
Merit_df.head()

NoticeDate_df= Merit_df.groupby(Merit_df["Notice Date"].dt.strftime("%b %Y"))["Diff Notice & Term (Days)"].mean().reset_index()
NoticeDate_df["Notice Date"] = NoticeDate_df["Notice Date"].apply(lambda x: datetime.datetime.strptime(x,"%b %Y"))
NoticeDate_df = NoticeDate_df.sort_values(by=["Notice Date"], ascending=True)
NoticeDate_df["Notice Date"] = NoticeDate_df["Notice Date"].apply(lambda x: x.strftime("%b %Y"))
print(NoticeDate_df)

NoticeDate_df.plot.bar(x="Notice Date", y="Diff Notice & Term (Days)")
plt.title('Bar chart of Time Taken to Terminate from Notice Date')
plt.xlabel('Date')
plt.ylabel('Number of Days')
plt.show()

DateAppoint_df = Merit_df.groupby(Merit_df["Date Appointed"].dt.strftime("%b %Y"))["Diff Appoint & Notice (Days)"].mean()
DateAppoint_df.plot(kind='bar',figsize=(12,6), color="orange")
plt.title('Bar chart of Time Taken from Start Date to Notice Date')
plt.xlabel('Date')
plt.ylabel('Number of Days')
plt.show()
