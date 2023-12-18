import pandas as pd
import numpy as np
import copy

folderPathOld='/Users/mac/Dropbox/Vyshnav/Misc important/Rightmove_Results/COMPARE/'
filePathOld = folderPathOld + '02_raw_BEFORE.csv'

folderPathNew ='/Users/mac/PycharmProjects/Random/csvs/'
filePathNew = folderPathNew+ '02_raw.csv'

df_old = pd.read_csv(filePathOld)
df_new = pd.read_csv(filePathNew)

df_new['Run_Date'] = pd.to_datetime(df_new['Run_Date'], format='%d/%m/%y')

df_new['Status_Date'] = pd.to_datetime(df_new['Status_Date'], format='%d/%m/%y')

df_old['Run_Date'] = pd.to_datetime(df_old['Run_Date'], format='%d/%m/%y')
df_old['Status_Date'] = pd.to_datetime(df_old['Status_Date'], format='%d/%m/%y')

filt1 = df_new['Status_Date'] >pd.Timestamp(2023,10,23)
df_new = df_new[filt1]

print(df_old.shape)
print(df_new.shape)
