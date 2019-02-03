#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/1/24 09:35
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : test3.py
import unittest
from selenium import webdriver
from config import chromedriver_path


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver_path)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
