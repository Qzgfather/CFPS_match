"""
date : 2019 03 06
author : 亓志国
本文件对最高教育程度进行编码和归一化处理，归一化后的结果在HDE_Coding.txt中
本文件只针对类别较少的特征！
"""

import pandas as pd
from Metadata.DATA import data

# HDE = data['tb4_a16_p'].value_counts()

"""
现在对文化程度特征进行编码；
内容                                                                               编码
Illiterate/Semi-literate                                                           0
Junior high school                                                                 9
Primary school                                                                     6
Senior high school/secondary school/technical school/vocational senior school      12
3-year college                                                                     15
4-year college                                                                     16
Not applicable                                                                     0
Master's degree                                                                    19
Missing                                                                            0
Unknown                                                                            0
Doctoral degree                                                                    22
Refuse                                                                             0
"""
# 获取原数据，进行循环编码

Lables = {"Illiterate/Semi-literate":0,
            "Junior high school": 9,
            "Primary school": 6,
            "Senior high school/secondary school/technical school/vocational senior school":12,
            "3-year college": 15,
            "4-year college": 16,
            "Not applicable": 0,
            "Master's degree": 19,
            "Missing": 0,
            "Unknown": 0,
            "Doctoral degree":22,
            "Refuse":0
          }
# 删除缺失值所在行的数据
HighestDegreeOfEducation = data()['tb4_a16_p']
F = HighestDegreeOfEducation.to_numpy()
# 将数据写入到txt文档中，方便后续的调用
HDE_File = open('..\\HandledFile\\HDE_Coding.txt', 'a')
# HDE_File.write('tb4_a16_p[HighestDegreeOfEducation]\n')
for i in F:
    HDE_File.write(str(int(Lables.get(i, 0))) + '\n')

HDE_File.close()
print('编码完成!')
