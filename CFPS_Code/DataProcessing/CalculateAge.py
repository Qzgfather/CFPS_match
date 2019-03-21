"""
date:2019 03 10
author:亓志国
本文件是计算样本的年龄，计算结果在Age.txt文件中，供后续的使用。
"""
from Metadata.DATA import data
BirthOfYear = data()['tb1y_a_p']
OtherState = frozenset(["Not applicable", "Missing"])
AgeFile = open("..\\HandledFile\\Age.txt", "a")
# AgeFile.write("tb1y_a_p[BirthOfYear,Now There Are Information Of Age]" + "\n")
for _ in BirthOfYear:
    if str(_) in OtherState:
        AgeFile.write("Error\n")
    else:
        AgeFile.write(str(2019.0 - float(_)) + "\n")

print("计算完毕，如需查看请打开Age.txt文件进行查看。")
AgeFile.close()