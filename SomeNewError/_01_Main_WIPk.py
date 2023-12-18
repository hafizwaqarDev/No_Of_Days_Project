from _02_raws import CLASS02_RAW
from _03_Unique_property_data import CLASS03_AGGREGATE
from _04_Delta_data import CLASS04_LATEST
from _05_Unique_property_Report import CLASS_5_REPORT_Unique_property
from _06_Delta_property_Report import CLASS_6_REPORT_Delta_property
from tools.removeFiles import removeFilesInCSVFolder
import pandas as pd

class CLASS_MAIN:
    def __init__(self):

        removeFilesInCSVFolder()

        folderPath ='/Users/mac/PycharmProjects/Random/csvs/'
        # folderPath = r'C:\Users\Muhammad Ahmad\Desktop\SomeNewError'
        filePath2 = folderPath+ '02_raw.csv'
        filePath3a = folderPath + '03_unique_property1.csv'
        filePath3b = folderPath + '03_UNIQUE_PROPERTY_DATA.csv'
        filePath4a = folderPath + '04a_DELTA_raw_SLICED.csv'
        filePath4b = folderPath + '04b_DELTA_UNIQUE_PROPERTY_SLICED.csv'
        filePath5a = folderPath + '05a_REPORT_UNIQUE_TABLE1.csv'
        filePath5b = folderPath + '05b_REPORT_UNIQUE_TABLE1.csv'
        filePath6a = folderPath + '06a_REPORT_DELTA_status.csv'

        #--- DF 2 ---------------------------
        df2_raw=CLASS02_RAW().df2_raw
        df2_raw.to_csv(filePath2)
        # --- DF 3 ---------------------------
        agg_obj = CLASS03_AGGREGATE(df2_raw)

        df3_UNIQUE_PROPERTY_DATA = agg_obj.df_aggregate2
        df3_UNIQUE_PROPERTY_DATA.to_csv(filePath3b)

        # --- DF 4 ---------------------------
        timeStampObj = pd.Timestamp(2023,10,23)
        obj4 = CLASS04_LATEST(df2_raw,timeStampObj)
        df4a = obj4.raw_df_sliced
        df4a.to_csv(filePath4a)

        df4_DELTA_PROPERTY_DATA = obj4.raw_df_sliced_agg
        df4_DELTA_PROPERTY_DATA.to_csv(filePath4b)

        # --- DF 5 ---------------------------
        obj5 = CLASS_5_REPORT_Unique_property(df3_UNIQUE_PROPERTY_DATA)
        df_list = obj5.table_1_df_list

        with open(filePath5a,'a') as f:
            for df in df_list:
                #print(df)
                df.to_csv(f)
                f.write("\n")


        # --- DF 6 ---------------------------
        obj6 = CLASS_6_REPORT_Delta_property(df4_DELTA_PROPERTY_DATA)
        df6a = obj6.delta_df_status
        df6a.to_csv(filePath6a)





CLASS_MAIN()