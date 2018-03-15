# -*- coding: utf-8 -*-
"""
Copyright (C) 2018, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of MIT license

<https://opensource.org/licenses/MIT>
"""
import logging
import json
import sys
import os
from pathlib import Path

class BpnConfig:
    
    #建構子
    def __init__(self):
        self.strConfigFilePath = os.sep.join((str(Path.home()), "bpn_conf.json"))
        self.intSellingPrice = 0
        self.intBuyingPrice = sys.maxsize
        
    #設定 提醒買價與賣價
    def setNotifyPrice(self, intBuyingPrice=sys.maxsize, intSellingPrice=0):
        self.intSellingPrice = intSellingPrice
        self.intBuyingPrice = intBuyingPrice
        
    #將設定檔回復為預設值
    def resetToDefaultConfig(self):
        #刪除舊的設定檔
        if os.path.exists(self.strConfigFilePath):
            os.remove(self.strConfigFilePath)
        #回復 Instance 變數為 預設值
        self.intSellingPrice = 0
        self.intBuyingPrice = sys.maxsize
        #儲存
        self.saveToConfigFile()
        
    #儲存設定
    def saveToConfigFile(self):
        dicBpnConfig = {
            "NotifyPrice":{
                "intSellingPrice": self.intSellingPrice,
                "intBuyingPrice": self.intBuyingPrice,
            }
        }
        self.writeDictToJsonFile(dicData=dicBpnConfig, strJsonFilePath=self.strConfigFilePath)
    
    #讀取設定
    def loadFromConfigFile(self):
        dicBpnConfig = self.readDictFromJsonFile(strJsonFilePath=self.strConfigFilePath)
        self.intSellingPrice = dicBpnConfig.get("NotifyPrice", {}).get("intSellingPrice", 0)
        self.intBuyingPrice = dicBpnConfig.get("NotifyPrice", {}).get("intBuyingPrice", sys.maxsize)
    
    #將 dict 物件的內容寫入到 json 檔案內
    def writeDictToJsonFile(self, dicData=None, strJsonFilePath=None):
        with open(strJsonFilePath, "w+") as jsonFile:
            jsonFile.write(json.dumps(dicData, ensure_ascii=False, indent=4, sort_keys=True))
            
    #讀取 json 檔案內容，回傳 dict 物件
    def readDictFromJsonFile(self, strJsonFilePath=None):
        dicRet = None
        with open(strJsonFilePath, "r") as jsonFile:
            dicRet = json.load(jsonFile, encoding="utf-8")
        return dicRet