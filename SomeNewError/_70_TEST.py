import pandas as pd
import numpy as np
import copy

folderPathOld='/Users/mac/Dropbox/Vyshnav/Misc important/Rightmove_Results/COMPARE/'
# folderPathOld=r'C:\Users\Muhammad Ahmad\Desktop\SomeNewError'
filePathOld = folderPathOld + '02_raw_BEFORE.csv'
# folderPathNew =r'C:\Users\Muhammad Ahmad\Desktop\SomeNewError'
folderPathNew ='/Users/mac/PycharmProjects/Random/csvs/'
filePathNew = folderPathNew+ '02_raw.csv'

# folderPathWrite = r'C:\Users\Muhammad Ahmad\Desktop\SomeNewError'
folderPathWrite = '/Users/mac/PycharmProjects/Random/csvs/'
filePathWrite1= folderPathWrite+'_07_old.csv'
filePathWrite2= folderPathWrite+'_07_new.csv'
filePathWrite3= folderPathWrite+'_07_diff.csv'

df_old = pd.read_csv(filePathOld)
df_new = pd.read_csv(filePathNew)

df_new['Run_Date'] = pd.to_datetime(df_new['Run_Date'], format='%Y-%m-%d')
df_new['Status_Date'] = pd.to_datetime(df_new['Status_Date'], format='%Y-%m-%d')
df_old['Run_Date'] = pd.to_datetime(df_old['Run_Date'], format='%Y-%m-%d')
df_old['Status_Date'] = pd.to_datetime(df_old['Status_Date'], format='%Y-%m-%d')

sortCol = ['Property_Unique_Number','Version_Number']
df_old.sort_values(sortCol,inplace=True)
df_new.sort_values(sortCol,inplace=True)
df_old.index.name='sNo'
df_new.index.name='sNo'

filt1 = df_new['Status_Date'] <= pd.Timestamp(2023,10,30)
#df_new = df_new[filt1]

if df_old.shape == df_new.shape:
    diff = df_new.compare(df_old,align_axis=1)
    diff.to_csv(filePathWrite3)
    print('diffed')
else:
    diff = pd.merge(df_old, df_new, on=sortCol, how="outer", indicator="Exists")
    diff.to_csv(filePathWrite3)

