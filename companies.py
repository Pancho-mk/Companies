import requests
from bs4 import BeautifulSoup
#import re
import csv
import pandas as pd
import numpy as np
#import xlsxwriter 

url = "https://en.wikipedia.org/wiki/List_of_companies_of_Switzerland"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")   #or html.parser

table_com = soup.findAll('table', class_='wikitable sortable')

table_com2 = table_com[1]
table_rows = table_com2.find_all('tr')   #finding all table rows

results = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip("\n") for i in td]
    results.append(row)

clean_results = results[1:]

#Making pandas dataframe from the table list: clean_result
df = pd.DataFrame(clean_results, columns=['Name', 'Industry', 'Sector', 'Headquarters', 'Founded', 'Notes'])

print(df.info())

#Transfering pandas dataframe to csv file
df.to_csv('results.csv') 
  
# Reading the csv file 
df_new = pd.read_csv('results.csv') 
  
# saving xlsx file 
comp_xl = pd.ExcelWriter('results.xlsx') 
df_new.to_excel(comp_xl, index = False) 
  
comp_xl.save() 




