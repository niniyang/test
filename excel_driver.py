# -*- coding:utf-8 -*-
# @Project: cema
# @Time : 2022/8/3 下午3:23
# @Author : yxl
# @File : excel_driver.py
import openpyxl


# class ExcelDriver:
excel = openpyxl.load_workbook('data/test.xlsx')
sheet = excel['Sheet1']
for values in sheet.values:
    if type(values[0]) is int:
        print(values)

