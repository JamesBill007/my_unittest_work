"""
======================
@author:LiXuejin

@time:2019/10/27:11:30

@email:lixuejin@fang.com
======================
"""
import unittest
from unittest_exercise.lib import HTMLTestRunnerNew
from unittest_exercise.scripts.context import CASES_PATH, REPORT_FILE

suite = unittest.TestSuite()
loader = unittest.TestLoader()

suite.addTests(loader.discover(CASES_PATH))

with open(REPORT_FILE, mode="wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="小测试",
                                              description="练习unittest框架")
    runner.run(suite)
