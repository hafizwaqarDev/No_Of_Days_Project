import pandas as pd
from _03_Unique_property_data import CLASS03_AGGREGATE
import copy


class CLASS04_LATEST:
    def __init__(self,raw_df, timeStampObj):
        self.__fn1_slice(raw_df,timeStampObj)
        self.__fn2_unique_prop_from_slice()


    def __fn1_slice(self,raw_df,timeStampObj):
        raw_df = copy.deepcopy(raw_df)
        raw_df.sort_values(by='Status_Date', ascending=True, inplace=True)
  
        raw_df['Run_Date'] = pd.to_datetime(raw_df['Run_Date'], format='%d/%m/%y')
        raw_df['Status_Date'] = pd.to_datetime(raw_df['Status_Date'], format='%d/%m/%y')
        filt1 = raw_df['Status_Date'] >timeStampObj
        sliced_raw = raw_df[filt1]
        sliced_raw = copy.deepcopy(sliced_raw)

        sliced_raw.sort_values(by='Property_Unique_Number', ascending=True, inplace=True)
        self.__sliced_raw=sliced_raw

    def __fn2_unique_prop_from_slice(self):

        sliced_agg=CLASS03_AGGREGATE(self.__sliced_raw).df_aggregate2
        sliced_agg.sort_values(by='Property_Unique_Number', ascending=True, inplace=True)
        self.__sliced_agg = sliced_agg



    @property
    def raw_df_sliced(self):
        return self.__sliced_raw

    @property
    def raw_df_sliced_agg(self):
        return self.__sliced_agg


