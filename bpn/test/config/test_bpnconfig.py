# -*- coding: utf-8 -*-
"""
Copyright (C) 2018, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of MIT license

<https://opensource.org/licenses/MIT>
"""
import unittest
import logging
import sys
from bpn.config import bpnconfig

"""
測試 設定檔 存取
"""

class BpnConfigTest(unittest.TestCase):

    #準備
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.bpnconfig = bpnconfig.BpnConfig()
        self.bpnconfig.resetToDefaultConfig() #初始化設定檔
        
    #收尾
    def tearDown(self):
        pass

    #測試 saveToConfigFile
    def test_saveToConfigFileAndLoadFromConfigFile(self):
        logging.info("BpnConfigTest.test_saveToConfigFile")
        #驗證初始設定
        self.assertEqual(self.bpnconfig.intSellingPrice, 0)
        self.assertEqual(self.bpnconfig.intBuyingPrice, sys.maxsize)
        #儲存新數值
        self.bpnconfig.setNotifyPrice(intBuyingPrice=200000, intSellingPrice=500000)
        self.bpnconfig.saveToConfigFile()
        #讀取
        self.bpnconfig.loadFromConfigFile()
        #驗證新數值
        self.assertEqual(self.bpnconfig.intSellingPrice, 500000)
        self.assertEqual(self.bpnconfig.intBuyingPrice, 200000)
        #回復為預設值
        self.bpnconfig.resetToDefaultConfig()
        #驗證 回復為預設值
        self.assertEqual(self.bpnconfig.intSellingPrice, 0)
        self.assertEqual(self.bpnconfig.intBuyingPrice, sys.maxsize)

#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


