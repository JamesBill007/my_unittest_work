"""
======================
@author:LiXuejin

@time:2019/10/26:21:03

@email:lixuejin@fang.com
======================
"""
import unittest
from lib import ddt
from scripts.read_excel import ReadExcel
from scripts.register import register
from scripts.mylogger import logger
from scripts.context import DATA_PATH_FILE

@ddt.ddt
class TestRegister(unittest.TestCase):

    rd = ReadExcel(DATA_PATH_FILE, "sheet")
    cases = rd.read_excel()

    @ddt.data(*cases)
    def test_register(self, items):
        excepted = items.excepted
        res = register(*eval(items.data))

        try:
            self.assertEqual(eval(excepted), res)
        except AssertionError as e:
            self.rd.write(items.case_id + 1, 5, "未通过")
            logger.info("{}用例测试未通过！异常为:{}".format(items.title, e))
            raise e

        else:
            logger.info(items.title + "用例测试通过")
            self.rd.write(items.case_id + 1, 5, "通过")


if __name__ == '__main__':
    unittest.main()