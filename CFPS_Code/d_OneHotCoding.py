"""
date:2019 03 07
author: 亓志国
本文件是对个体的最高受教育程度进行独热值编码，编码结果在HDE_Coding.txt文件中。
"""
from Metadata.DATA import data
from sklearn.preprocessing import OneHotEncoder
import os
data = data().dropna()
HighestDegreeOfEducation = data()['tb4_a16_p']
X = HighestDegreeOfEducation.to_numpy().reshape(-1, 1)
enc = OneHotEncoder(categories='auto').fit(X)
FeatureName = OneHotEncoder(categories='auto').fit(X).get_feature_names()
result = enc.transform(X).toarray()
File_state = os.listdir(path=".\\HandledFile\\")
if 'HDE_Coding.txt' in File_state:
    raise ValueError("文件已经存在!请删除HDE_Coding.txt文件重新运行。")
else:
    pass
f = open('HDE_Coding.txt', 'a')
f.write('tb4_a16_p[HighestDegreeOfEducation]' + '\n' + str(FeatureName) + '\n')
for i in result:
    f.write(str(i) + '\n')

f.close()
print("编码完毕，请查看HandledFile文件及下的HDE_Coding.txt文件。")
