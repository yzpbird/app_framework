#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:bird
@file: login_page_locs.py
@time: 2020/09/01
"""
from appium.webdriver.common.mobileby import MobileBy

class LoginPageLocs:

    # 用户头像
    login_avatar_loc = (MobileBy.ID, "com.lemon.lemonban:id/fragment_my_lemon_avatar_image")

    # 用户名文本元素
    avatar_title_loc = "com.lemon.lemonban:id/fragment_my_lemon_avatar_title"

    # 用户名输入框
    user_input_loc = (MobileBy.ID, "com.lemon.lemonban:id/et_mobile")
    # 密码输入框
    passwd_input_loc = (MobileBy.ID, "com.lemon.lemonban:id/et_password")
    # 登录按钮
    login_button_loc = (MobileBy.ID, "com.lemon.lemonban:id/btn_login")
