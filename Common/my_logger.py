"""
定制我的日志类：
1、创建一个日志收集器、设定输出级别。
2、设定我固定的日志内容呈现格式
3、输出日志到控制台和文件

info()  error()  debug() warning()  exception() critical()
"""
import logging
from logging import handlers
import os
from Common.handle_path import logs_dir


class MyLogger(logging.Logger):

    def __init__(self,name,level="INFO",file=None):
        super().__init__(name,level)

        # Formatter类，设置输出内容呈现
        fmt = "%(asctime)s %(name)s:%(levelname)s:%(filename)s【%(lineno)d】: %(message)s"
        ft = logging.Formatter(fmt)

        # 创建一个控制台渠道。
        handle1 = logging.StreamHandler()
        handle1.setFormatter(ft)
        # 将控制台渠道添加到 日志收集器当中。
        self.addHandler(handle1)

        # 创建一个文件渠道
        if file:
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(ft)
            # 将文件渠道都添加到 日志收集器当中。
            self.addHandler(handle2)

print(os.path.join(logs_dir, "apptest.log"))
logger = MyLogger("app_framework",file=os.path.join(logs_dir, "apptest.log"))


if __name__ == '__main__':
    logger.info('66666')

# m = MyLogger("java17","INFO",r'D:\Pychram-Workspace\java17\class_logging\java17-22.log')
# m.warning("111111111111111111")