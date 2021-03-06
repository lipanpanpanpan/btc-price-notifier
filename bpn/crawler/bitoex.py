# -*- coding: utf-8 -*-
"""
Copyright (C) 2018, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of MIT license

<https://opensource.org/licenses/MIT>
"""
from selenium import webdriver
import pkg_resources
import logging
import time
import random
import re
import os

"""
抓取 https://www.bitoex.com/charts?locale=zh-tw 即時匯率
"""
class CurrentPriceCharts:
    
    #建構子
    def __init__(self):
        self.driver = None
        self.intCurrentBuyingPrice = 0
        self.intCurrentSellingPrice = 0
        
    #取得 selenium driver 物件
    def getDriver(self):
        driver = None
        #phantomjs driver
        chromeDriverExeFilePath = pkg_resources.resource_filename("bpn.resource", "chromedriver.exe")
        #chrome 選項
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome(chromeDriverExeFilePath, options=options)
        return driver
    
    #初始化 selenium driver 物件
    def initDriver(self):
        if self.driver is None:
            self.driver = self.getDriver()
        
    #終止 selenium driver 物件
    def quitDriver(self):
        self.driver.quit()
        self.driver = None
        
    #執行 crawler
    def runCrawler(self):
        self.initDriver() #init selenium driver
        self.getCurrentBuyingAndSellingPrice()
        self.quitDriver() #quit selenium driver
    
    #取得買賣現價
    def getCurrentBuyingAndSellingPrice(self):
        self.driver.get("https://www.bitoex.com/charts?locale=zh-tw")
        time.sleep(random.randint(5, 10))
        strCurrentBuyingPrice = self.driver.find_element_by_css_selector("div.buy h4.sync_rate_buy span").text
        strCurrentSellingPrice = self.driver.find_element_by_css_selector("div.sell h4.sync_rate_sell span").text
        intCurrentBuyingPrice = int(re.sub(r"[^0-9]+", "", strCurrentBuyingPrice))
        intCurrentSellingPrice = int(re.sub(r"[^0-9]+", "", strCurrentSellingPrice))
        (self.intCurrentBuyingPrice, self.intCurrentSellingPrice) = (intCurrentBuyingPrice, intCurrentSellingPrice)
    