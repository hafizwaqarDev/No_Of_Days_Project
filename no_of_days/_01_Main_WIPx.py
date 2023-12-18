from _02_raws import CLASS02_RAW
from _03_Unique_property_data import CLASS03_AGGREGATE
from _04_Delta_data import CLASS04_LATEST
from _05_Report import CLASS_REPORT1_Unique_property

class CLASS_MAIN:
    def __init__(self):
        folderPath = r'C:\Users\Muhammad Ahmad\Desktop\no_of_days\no_of_days'
        # folderPath ='/Users/mac/PycharmProjects/Random/csvs/'
        filePath2 = folderPath+ '02_raw.csv'
        filePath3a = folderPath + '03_unique_property1.csv'
        filePath3b = folderPath + '03_UNIQUE_PROPERTY_DATA.csv'
        filePath4a = folderPath + '04a_DELTA_raw_SLICED.csv'
        filePath4b = folderPath + '04b_DELTA_UNIQUE_PROPERTY_SLICED.csv'
        filePath4c = folderPath + '04c_DELTA_GROUPED_status.csv'


        #--- DF 2 ---------------------------
        df2_raw=CLASS02_RAW().df2_raw
        df2_raw.to_csv(filePath2)

        # --- DF 3 ---------------------------
        agg_obj = CLASS03_AGGREGATE(df2_raw)

        df3_agg2 = agg_obj.df_aggregate2
        df3_agg2.to_csv(filePath3b)

        dfX_UNIQUE_PROPERTY_DATA = df3_agg2

        # --- DF 4 ---------------------------
        obj4 = CLASS04_LATEST(df2_raw)
        df4a = obj4.raw_df_sliced
        df4a.to_csv(filePath4a)

        df4b = obj4.raw_df_sliced_agg
        df4b.to_csv(filePath4b)

        df4c = obj4.grouped_df_status
        df4c.to_csv(filePath4c)


        dfY_DELTA_PROPERTY_DATA = df4a

        # --- DF 5 ---------------------------

        obj5 = CLASS_REPORT1_Unique_property(dfX_UNIQUE_PROPERTY_DATA)

CLASS_MAIN()