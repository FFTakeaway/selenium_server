# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:45:10 2020

@author: lemar
"""

from flask import Flask, json
from selenium import webdriver
#import pandas as pd

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/rushing', methods=['GET'])
def get_rushing():
    driver = webdriver.Chrome(executable_path = r"C:/Users/lemar/Desktop/Schoolwork/Senior Design 2/chromedriver_win32/chromedriver.exe") 
    url = "https://www.pro-football-reference.com/years/2019/rushing_advanced.htm"
    #load the page
    driver.get(url)
    rushing_info = { "html" : str(driver.page_source)}
    #rushing_info = { "html" :  "rushing info"}
    return json.dumps(rushing_info)

if __name__ == '__main__':
    print("server up")
    api.run()