# -*- coding: utf-8 -*-
"""
Copyright (C) 2018, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of MIT license

<https://opensource.org/licenses/MIT>
"""
import unittest
import logging
from bpn.crawler import bitoex

"""
測試 幣託 爬蟲
"""

class CurrentPriceChartsTest(unittest.TestCase):

    #準備
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.crawler = bitoex.CurrentPriceCharts()
        
    #收尾
    def tearDown(self):
        pass

    #測試 getBuyingAndSellingPrice
    def test_runCrawler(self):
        logging.info("CurrentPriceChartsTest.test_runCrawler")
        self.crawler.runCrawler()

#測試開始
if __name__ == "__main__":
    unittest.main(exit=False)


