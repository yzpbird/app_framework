#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:bird
@file: handle_path.py
@time: 2020/09/03
"""

import os

# 得到当前项目的根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
# 日志路径
logs_dir = os.path.join(base_dir, "Outputs", "logs")
# 截图路径
screenshots_dir = os.path.join(base_dir, "Outputs", "screenshots")
# 报告路径
reports_dir = os.path.join(base_dir, "Outputs", "reports")