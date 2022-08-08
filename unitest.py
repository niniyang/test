# -*- coding:utf-8 -*-
# @Project: cema
# @Time : 2022/8/4 下午5:12
# @Author : yxl
# @File : unitest.py
import unittest

from ddt import ddt, data

from class02.keys import Keys

@ddt
class TestDemo(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.key = Keys('Chrome')
    #
    # def setUp(self) -> None:
    #     print('setup')
    #
    # def tearDown(self) -> None:
    #     print('teardown')
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.key.quit()

    @data
    def test_01(self):
        print('test01')


if __name__ == '__main__':
    unittest.main()
