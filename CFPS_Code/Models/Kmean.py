from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Metadata.DATA import data
FamilyID = data()["fid16"]
F = open("..\\HandledFile\\Age.txt", "r")
Age = F.readlines()
AgeList = []
for i in Age:
    if  "E" in i:
        AgeList.append(0)
    else:
        AgeList.append(i[:-1])
AgeDict = {"Age": AgeList}
print(AgeDict)

UrbanList = []

F2 = open("..\\HandledFile\\Urban.txt", "r")
Urban = F2.readlines()
for i in Urban:
    if "U" in i :
        UrbanList.append(1)
    elif "R" in i:
        UrbanList.append(2)
    else:
        UrbanList.append(0)
UrbanDict = {"Urban": UrbanList}
print(UrbanDict)

HDEList = []
F3 = open("..\\HandledFile\\HDE_Coding.txt", "r")
HDE = F3.readlines()
for i in HDE:
    HDEList.append(i[:-1])
HDE = {"HDE": HDEList}

# 画图
# 绘制散点图
X1 = pd.DataFrame(AgeDict)
X2 = pd.DataFrame(UrbanDict)
X3 = pd.DataFrame(HDE)

x = AgeDict["Age"]
y = HDE["HDE"]
z =  UrbanDict["Urban"]


fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)

# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('Z', fontdict={'size': 2, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 2, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 2, 'color': 'red'})
# plt.show()


X = pd.merge(X1, X2, left_index=True, right_index=True)
X = pd.merge(X, X3, left_index=True, right_index=True)
# print(X)

n = 3

cluster = KMeans(n_clusters=n, random_state=0).fit(X)
print(cluster.labels_)
n = 0
NList = []
NList2 = []
NList3 = []

for i in cluster.labels_:
    i = str(i)
    if i == "1":
        NList.append(n)
    else:
        pass
    n += 1

for i in NList:
    NList2.append(i + 1)
print(NList2)
print(len(NList2))
for i in NList2:
    i = int(i)
    NList3.append(FamilyID.to_numpy()[i - 1])

print(NList3)

F = open("..\\HandledFile\\FinalData.txt", "a")
for i in NList3:
    F.write(str(i) + "\n")
F.close()