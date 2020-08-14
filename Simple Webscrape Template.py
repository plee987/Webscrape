# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:18:10 2020

@author: Paul
"""

import requests
import pandas as pd

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
pd.options.display.max_rows = 150
pd.options.display.max_columns = 150
pd.options.display.width = 300

url = # Enter website url
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df.to_csv(# Specify file name with .csv extension)

print(df)
import time
TodaysDate = time.strftime("%m-%d-%Y")
excelfilename = #Specify filepath_" + TodaysDate +".xlsx"

df.to_excel(excelfilename, index = False, header = True)