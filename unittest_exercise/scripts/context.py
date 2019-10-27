"""
======================
@author:LiXuejin

@time:2019/10/27:9:14

@email:lixuejin@fang.com
======================
"""
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
# print(BASE_PATH)
CASES_PATH = os.path.join(BASE_PATH, "cases")
# print(CASES_PATH)
DATA_PATH = os.path.join(BASE_PATH, "data")
DATA_PATH_FILE = os.path.join(DATA_PATH, "register_data.xlsx")
# print(DATA_PATH_FILE)
REPORT = os.path.join(BASE_PATH, "report")
REPORT_FILE = os.path.join(REPORT, "report.html")
# print(REPORT_FILE)