from Metadata.DATA import data
Urban = data()["fid_urban16"].to_numpy()
# print(Urban.value_counts())
# print(Urban[0])
UrbanFile= open(".\\HandledFile\\Urban.txt", "a")
for i in Urban:
    UrbanFile.write(i + "\n")

UrbanFile.close()

