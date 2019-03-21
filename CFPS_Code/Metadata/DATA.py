"""
date:2019 03 06
author:亓志国
本文档用于转换元数据，将元数据转换为pandas中的DataFrame格式，供全项目使用.
并去除了缺失项所在行的数据
"""
import pandas as pd


def data():
    Global_data = pd.read_stata('..\\data\\ecfps2016famconf_201804.dta')
    Global_data = Global_data.dropna()
    return Global_data
