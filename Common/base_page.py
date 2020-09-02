#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:bird
@file: base_page.py
@time: 2020/09/01
"""

"""
1、封装app当中元素的基本操作
    等待元素可见
    查找元素
    元素的输入内容:    等待元素可见+查找元素+元素输入
    元素的点击:        等待元素可见+查找元素+元素点击      
    获取元素的文本:    等待元素存在+查找元素+获取元素文本
    获取元素的属性:    等待元素存在+查找元素+获取元素属性
    
2、基本操作加入日志和失败截图
    
"""

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.my_logger import logger
import time


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, img_desc="", timeout=10, poll_frequency=0.5):
        """
        等待元素可见
        @param loc: 元素
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @param timeout:  超时时间，默认10s
        @param poll_frequency:  轮询频率,默认0.5
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            logger.exception("等待元素可见失败: {}".format(loc))
            # 失败截图 - 截图命名
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("{} 等待 {} 元素可见成功。".format(img_desc, loc))

    def wait_page_contains_ele(self, loc, img_desc="", timeout=10, poll_frequency=0.5):
        """
        等待页面是否包含元素
        @param loc: 元素定位
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @param timeout: 超时时间，默认10
        @param poll_frequency: 轮询频率,默认0.5
        """
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_all_elements_located(loc))
        except:
            logger.exception("等待元素存在失败: {}".format(loc))
            # 失败截图 - 截图命名
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("{} 等待 {} 元素存在成功。".format(img_desc, loc))

    def get_element(self, loc, img_desc=""):
        """
        查找元素
        @param loc: 元素定位
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @return: 返回查找到的元素
        """
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception("查找元素失败: {}".format(loc))
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("查找元素 {} 成功。".format(loc))
            return ele

    def click_element(self, loc, img_desc="", timeout=10, poll_frequency=0.5):
        """
        点击元素
        @param loc:  元素定位
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @param timeout: 超时时间,默认10s
        @param poll_frequency: 轮询频率,默认0.5
        """
        self.wait_ele_visible(loc, img_desc, timeout, poll_frequency)
        ele = self.get_element(loc, img_desc)
        try:
            ele.click()
        except:
            logger.exception("点击元素失败: {}".format(loc))
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("点击元素 {} 成功。".format(loc))

    def input_text(self, loc, value, img_desc="", timeout=10, poll_frequency=0.5):
        """
        往元素中输入内容
        @param loc:  元素定位
        @param value:  输入值
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @param timeout: 超时时间,默认10s
        @param poll_frequency: 轮询频率,默认0.5
        """
        self.wait_ele_visible(loc, img_desc, timeout, poll_frequency)
        ele = self.get_element(loc, img_desc)
        try:
            ele.sendkeys(value)
        except:
            logger.exception("元素输入 {} 失败".format(loc))
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("元素输入 {} 成功。".format(loc))

    def get_ele_text(self, loc, img_desc="", timeout=20, poll_frequency=0.5):
        """
        获取元素的文本值
        @param loc: 元素定位
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @param timeout: 超时时间,默认10s
        @param poll_frequency: 轮询频率,默认0.5
        @return: 元素的文本值
        """
        self.wait_page_contains_ele(loc, img_desc, timeout, poll_frequency)
        ele = self.get_element(loc, img_desc)
        try:
            text = ele.text
        except:
            logger.exception("获取元素 {} 的文本值失败".format(loc))
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("元素 {} 的文本值为 {}".format(loc, text))
            return text

    def get_ele_attribute(self, loc, attr_name, img_desc="", timeout=10, poll_frequency=0.5):
        """
        获取元素的属性值
        @param loc: 元素定位
        @param attr_name: 属性名
        @param img_desc: 失败截图的命名：页面名称_功能名称
        @param timeout: 超时时间,默认10s
        @param poll_frequency: 轮询频率,默认0.5
        @return: 元素的属性值
        """
        self.wait_page_contains_ele(loc, img_desc, timeout, poll_frequency)
        ele = self.get_element(loc, img_desc)
        try:
            val = ele.get_attribute(attr_name)
        except:
            logger.exception("获取元素 {} 的属性值失败".format(loc))
            self.get_screenshot(img_desc)
            raise
        else:
            logger.info("元素 {} 的属性值为 {}".format(loc, val))
            return val

    def get_screenshot(self, img_desc):
        """
        失败截图
        @param img_desc: 失败截图的命名：页面名称_功能名称
        """
        # 处理好截图命名： 页面名称_功能名称_截图时间
        now = time.strftime("%Y-$m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_desc, now)
        # 截图操作
        self.driver.save_screenshot(filepath)
        logger.info("截取当前页面，截图路径为: {}".format(filepath))


if __name__ == '__main__':
    pass
