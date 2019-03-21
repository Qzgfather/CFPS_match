from Metadata.DATA import data
FamilyID = data()["fid16"]
StillAlive = data()["alive_a16_p"]
# print(FamilyID[0])
# print(StillAlive[0])
# quit()
f = open(".\\HandledFile\\data.txt", 'r')
ff = f.readlines()
n = 2
# 注：储存的是FID16中家庭中只有一个人的数据，与下面的存储索引的列表区分
OnePeople = []
# 循环读取数据
for i in ff:
    try:
        if int(i[-3:]) != 1:
            pass
        else:
            OnePeople.append(int(eval(i[:-3])))
    except:
        pass
print("这是家庭中仅为一人的FID16编号：{0:}".format(OnePeople))
# 存储所有样本的的索引！注意 是索引！
Code = []
# 通过对编码进行索引获取样本死亡的索引，请注意是索引！
# 如果一个样本死亡，此列表将存储他的序列 并从Code中剔除
StateOfAlive = []
# 用来储存存活样本的索引！
FinalList = []
# print(OnePeople)

for i in OnePeople:

    Code.append(list(FamilyID.isin([i])).index(True) + 1)

    # print(FamilyID.isin(int(i)))
    # quit()
    # Code.append(list(FamilyID.isin(int(i))).index(True) + 1)

print("所有家庭中仅为一人的家庭索引：{0:}".format(Code))


