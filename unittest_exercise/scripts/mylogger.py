"""
======================
@author:LiXuejin

@time:2019/10/31:22:55

@email:lixuejin@fang.com
======================
"""
import logging
from logging.handlers import RotatingFileHandler
from scripts.context import LOG_PATH_FILE


class MyLogger(object):

    def __init__(self):
        # 创建一个日志收集器
        self.my_log = logging.getLogger("log")
        # 设置日志收集器的等级
        self.my_log.setLevel("INFO")
        # 定义日志收集器的渠道
        self.console_handler = logging.StreamHandler()  # 输出控制台
        # 输出到文件
        self.file_handler = RotatingFileHandler(filename=LOG_PATH_FILE,
                                                mode="a",
                                                maxBytes=1024 * 1024,
                                                backupCount=3,
                                                encoding="utf-8")

        # 设置日志输入渠道的等级
        self.console_handler.setLevel("INFO")
        self.file_handler.setLevel("INFO")
        # 设置日志输出格式
        formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(module)s - %(name)s - "
                                      "%(lineno)d - [日志信息]:%(message)s")
        self.console_handler.setFormatter(formatter)
        self.file_handler.setFormatter(formatter)

        # 对接渠道
        self.my_log.addHandler(self.console_handler)
        self.my_log.addHandler(self.file_handler)

    def get_logger(self):
        return self.my_log


logger = MyLogger().get_logger()

if __name__ == '__main__':
    logger = MyLogger().get_logger()
    logger.info("ceshi")
