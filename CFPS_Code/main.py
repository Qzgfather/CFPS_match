F1 = open(".\\HandledFile\\FinalData.txt", "r")
F2 = open(".\\HandledFile\\OnePeople.txt", "r")

OnePeople = []
OnePeople4 = []
for i in F2.readlines():
    OnePeople.append(int(eval(i[:-3])))


OnePeople2 = []
for i in F1.readlines():
    OnePeople2.append(int(eval(i)))



OnePeople3 = []
for i in OnePeople2:
    if i in OnePeople:
        OnePeople3.append(i)
    else:
        pass


F1.close()
F2.close()
for i in OnePeople2:
    if i in OnePeople3:
        pass
    else:
        OnePeople4.append(i)

print("最终预测结果为：{0:}".format(OnePeople3+OnePeople4[0:546]))
