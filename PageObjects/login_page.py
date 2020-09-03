#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:bird
@file: login_page.py
@time: 2020/09/01
"""
from appium.webdriver.webdriver import WebDriver
from PageLocators.login_page_locs import LoginPageLocs as locs
from Common.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, passwd):
        self.input_text(locs.user_input_loc, username, "登录页面_输入用户名")
        self.input_text(locs.passwd_input_loc, passwd, "登录页面_输入密码")
        self.click_element(locs.login_button_loc, "登录页面_点击登录按钮")