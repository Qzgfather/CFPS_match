from Metadata.DATA import data
FamilyID = data()["fid16"]
StillAlive = data()["alive_a16_p"]
# print(FamilyID[0])
# print(StillAlive[0])
# quit()
f = open("..\\HandledFile\\data.txt", 'r')
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

OnePeopleFile = open("..\\HandledFile\\OnePeopleData.txt", 'a')
for i in OnePeople:
    OnePeopleFile.write(str(i) + "\n")
OnePeopleFile.close()



