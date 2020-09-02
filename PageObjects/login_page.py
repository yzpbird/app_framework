#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:bird
@file: login_page.py
@time: 2020/09/01
"""
from appium.webdriver.webdriver import WebDriver
from PageLocators.login_page_locs import LoginPageLocs as locs

class LoginPage:

    def login(self, username, passwd):
        self.driver.find_element(*locs.user_input).send_keys(username)
        self.driver.find_element(*locs.passwd_input).send_keys(passwd)
        self.driver.find_element(*locs.login_button).click()