# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:37:25 2020

@author: lemar
"""

import requests 
import pandas as pd  

# api-endpoint 
URL = "https://webapi-hw2.herokuapp.com/advanced/rushing/2019"
  
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 
table = pd.read_html(data["html"])[0]
print(table)
