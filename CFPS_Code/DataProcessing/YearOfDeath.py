from Metadata.DATA import data
YearOfDeath = data()["ta4y_a16_p"]
YearOfBirth = data()["tb1y_a_p"]
n = 0
index = 0
YearOfLive = {}
error_num = 0
# 表示总存活时间，用于计算平均存活时间
Full = 0
for i in YearOfDeath:
    index += 1
    if isinstance(i, str):
        pass
    else:
        n += 1
        YearOfDeathCopy = YearOfDeath.to_numpy()[index - 1]
        YearOfBirthCopy = YearOfBirth.to_numpy()[index - 1]
        try:
            YearOfLives = YearOfDeathCopy - YearOfBirthCopy
            YearOfLive.update({index: YearOfLives})
        except:
            YearOfLive.update({index: "Error"})
            error_num += 1
print(n)
print(YearOfLive)
print("有{}个无法计算存活时间".format(error_num))
for values in YearOfLive.values():
    if values == "Error":
        pass
    else:
        Full += values
print(Full/(n-error_num))
