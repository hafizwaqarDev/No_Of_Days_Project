import pandas as pd
from _60_ADD import  fn_61_ADD_LATEST_STATUS, fn_62_ADD_LATEST_PRICE, fn_63_ADD_LATEST_STATUS_DATE, fn_64_ADD_FIRST_DATE, fn_65_ADD_Total_Days
import datetime as dt
from datetime import datetime

class CLASS03_AGGREGATE:
    def __init__(self, df1_raw):
        self.__df1_raw = df1_raw
        self.__fn1_create_simple_aggregate_df()
        self.__fn2_addtional_columns()
        
    def __fn1_create_simple_aggregate_df(self):
        groupByCols = ['Property_Unique_Number', 'Address', 'Bed_Rooms', 'Property_Type', 'Property_Url', 'Agent_Name',
                       'Location']

        dfGroupbyObj = self.__df1_raw.groupby(groupByCols)
        serX_agg = dfGroupbyObj.size()
        dfX_agg = pd.DataFrame(serX_agg)
        dfX_agg.reset_index(inplace=True)
        dfX_agg.index.name = 'propNum'
        groupByCols.append('versionCount')
        dfX_agg = dfX_agg.set_axis(groupByCols, axis=1)
        
        self.__df3a_simple_agg = dfX_agg
    
    def __fn2_addtional_columns(self):
        agg_df_01 = self.__df3a_simple_agg

        df_raw = self.__df1_raw
        raw_df_groupBy_obj = df_raw.groupby('Property_Unique_Number')
        ser_prop_num =agg_df_01['Property_Unique_Number']
        
        seriesLatestStatus = ser_prop_num.apply(fn_61_ADD_LATEST_STATUS, args=(raw_df_groupBy_obj,))
        seriesLatestStatus.name='last_status'

        seriesPrice = ser_prop_num.apply(fn_62_ADD_LATEST_PRICE, args=(raw_df_groupBy_obj,))
        seriesPrice.name = 'last_price'

        seriesStatusDate = ser_prop_num.apply(fn_63_ADD_LATEST_STATUS_DATE, args=(raw_df_groupBy_obj,))
        seriesStatusDate.name = 'last_stat_date'
        # print(seriesStatusDate)
        # print(type(seriesStatusDate))

        seriesFirstDate = ser_prop_num.apply(fn_64_ADD_FIRST_DATE, args=(raw_df_groupBy_obj,))
        seriesFirstDate.name = 'first_date'
        # print(seriesFirstDate)
        # print(type(seriesFirstDate))

        #-- AHMAD PLEASE WORK ON THIS--------------------------
        # New Column
        seriesNoOfDaysInMarket = ser_prop_num.apply(fn_65_ADD_Total_Days, args=(raw_df_groupBy_obj,))
        seriesNoOfDaysInMarket.name = 'No_of_Days'

        #------------------------------------------------------

        what2Concat = [agg_df_01, seriesLatestStatus,  seriesPrice, seriesStatusDate, seriesFirstDate, seriesNoOfDaysInMarket]
        df = pd.concat(what2Concat, axis=1)

        df.sort_values(by='Property_Unique_Number', ascending=True, inplace=True)

        self.__df3b_final_agg = df


    @property
    def df_aggregate2(self):
        return self.__df3b_final_agg



