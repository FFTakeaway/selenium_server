# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:45:10 2020

@author: lemar
"""

from flask import Flask, json
from selenium import webdriver
import os
#import urllib.parse as urlparse
#from urllib.parse import parse_qs
#import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

app = Flask(__name__)

@app.route('/rushing/<string:category>', methods=['GET'])
def get_rushing(category):
    print("received get request")
    url = "https://www.pro-football-reference.com/years/2019/rushing_advanced.htm"
    #load the page
    driver.get(url)
    print("got content")
    rushing_info = { "html" : str(driver.page_source), "category" : category}
    #rushing_info = { "html" :  "rushing info"}
    print("returning content")
    return json.dumps(rushing_info)

if __name__ == '__main__':
    print("server up")
    app.run()