from selenium import webdriver
import pandas as pd
import numpy as np
import time
import pyautogui
import xlrd
import matplotlib.pyplot as plt

####Fetch website and download Excel file
##
##browser = webdriver.Chrome('C:\\Users\\user\Desktop\chromedriver.exe')
##browser.get('https://www.w3resource.com/python-exercises/pandas/excel/index.php')
##
##time.sleep(10)
##
##pyautogui.click(835,969)
##
####elem = browser.find_element_by_css_selector('body > div.cc_banner-wrapper > div > a.cc_btn.cc_btn_accept_all')
####elem.click()
##
##
##elem = browser.find_element_by_css_selector('body > div.mdl-layout.mdl-layout--fixed-header > main > div > div > div.mdl-cell.mdl-card.mdl-shadow--2dp.through.mdl-shadow--6dp.mdl-cell--7-col > article > p:nth-child(46) > strong > a')
##elem.click()
##
##time.sleep(5)
##
##Exit browsers
##
##browser.close()
##browser.quit()
##
####Read Excel file
##
df = pd.read_excel("C:\\Users\\user\Downloads\coalpublic2013.xlsx", header=0, delim_whitespace=True)
##
####4. Write a Pandas program to find the sum, mean, max, min value of 'Production (short tons)' column of coalpublic2013.xlsx file
##
##print ("Sum: ", df["Production"].sum())
##print ("Mean: ", df["Production"].mean())
##print ("Maximum ", df["Production"].max())
##print ("Minimum ", df["Production"].min())
##
####5. Write a Pandas program to insert a column in the sixth position of the said excel sheet and fill it with NaN values
##
##print(df.insert(3, "column1", np.nan))
##
####6. Write a Pandas program to import excel data (coalpublic2013.xlsx ) skipping first twenty rows into a Pandas dataframe
##
####df = pd.read_excel("C:\\Users\\user\Downloads\coalpublic2013.xlsx", skiprows = 20)
####df
##
####7. Write a Pandas program to add summation to a row of the given excel file
##
##sum_row=df[["Production", "Labor_Hours"]].sum()
##df_sum=pd.DataFrame(data=sum_row).T
##df_sum=df_sum.reindex(columns=df.columns)
##df_sum
##
####8. Display last 10 rows and all rows
##
##print(df.tail(n=10))
##print(df.head(999))
##
####9. Write a Pandas program to create a subtotal of "Labor Hours" against MSHA ID from the given excel data (coalpublic2013.xlsx )
##
##df_sub = df[["MSHA ID","Labor_Hours"]].groupby('MSHA ID').sum()
##print(df_sub)
##
####10. Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find a specific MSHA ID
##
##print(df[df["MSHA ID"]==102901].head())
##
####11. Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Labor Hours" > 20000
##
##print(df[df.Labor_Hours > 20000])
##
####12. Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and find details where "Mine Name" starts with "P"
##
##print(df[df["Mine_Name"].map(lambda x: x.startswith('P'))].head())

####Practice Bar Plot
##ax = df[['Mine_Name','Production']].plot(kind='bar', title ="Production", figsize=(15, 10), legend=True, fontsize=12)
##ax.set_xlabel("Mine_Name", fontsize=12)
##ax.set_ylabel("Production", fontsize=12)
##plt.show()

##23. Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and draw a bar plot where each bar will represent one of the top 10 production

##sorted_by_production = df.sort_values(['Production'], ascending=False).head(10)
##sorted_by_production['Production'].head(10).plot(kind="barh")
##plt.show()

##24. Write a Pandas program to import excel data (coalpublic2013.xlsx ) into a dataframe and draw a bar plot comparing year, MSHA ID, Production and Labor_hours of first ten records.

df.head(999).plot(kind='bar', figsize=(20,8))
plt.show()


