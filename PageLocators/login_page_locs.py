#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:bird
@file: login_page_locs.py
@time: 2020/09/01
"""
from appium.webdriver.common.mobileby import MobileBy

class LoginPageLocs:

    # 用户名输入框
    user_input = (MobileBy.ID, "com.lemon.lemonban:id/et_mobile")
    # 密码输入框
    passwd_input = (MobileBy.ID, "com.lemon.lemonban:id/et_password")
    # 登录按钮
    login_button = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")
