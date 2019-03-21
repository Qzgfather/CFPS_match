from Metadata.DATA import data
import pandas as pd
FamilyID = data()["fid16"]
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
f = open(".\\HandledFile\\data.txt", 'a')
f.write(str(FamilyID.value_counts()))
