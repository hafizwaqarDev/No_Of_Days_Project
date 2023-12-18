import copy
import pandas as pd
from _03_Unique_property_data import CLASS03_AGGREGATE
import copy
from _50_REPLACE import CLASS_51_REPLACE_STATUS

class CLASS04_LATEST:
    def __init__(self,raw_df):
        self.__fn1_slice(raw_df)
        self.__fn2_unique_prop_from_slice()
        self.__fn3_group()


    def __fn1_slice(self,raw_df):
        raw_df = copy.deepcopy(raw_df)
        raw_df.sort_values(by='Status_Date', ascending=True, inplace=True)
  
        raw_df['Run_Date'] = pd.to_datetime(raw_df['Run_Date'], format='%d/%m/%y')
        raw_df['Status_Date'] = pd.to_datetime(raw_df['Status_Date'], format='%d/%m/%y')
        filt1 = raw_df['Status_Date'] >pd.Timestamp(2023,10,23)
        sliced_raw = raw_df[filt1]
        sliced_raw = copy.deepcopy(sliced_raw)

        sliced_raw.sort_values(by='Property_Unique_Number', ascending=True, inplace=True)
        self.__sliced_raw=sliced_raw

    def __fn2_unique_prop_from_slice(self):

        sliced_agg=CLASS03_AGGREGATE(self.__sliced_raw).df_aggregate2
        sliced_agg.sort_values(by='Property_Unique_Number', ascending=True, inplace=True)
        self.__sliced_agg = sliced_agg

    def __fn3_group(self):
        dfX = self.__sliced_agg
        dfX['last_status']=CLASS_51_REPLACE_STATUS(dfX['last_status']).series_updated_status
        groupByCols =['Location','last_status']

        #----------
        dfGroupbyObj = dfX.groupby(groupByCols)
        serX_agg = dfGroupbyObj.size()
        dfX_agg = pd.DataFrame(serX_agg)
        dfX_agg.reset_index(inplace=True)
        dfX_agg.index.name = 'statusNo'
        groupByCols.append('statusCount')
        dfX_agg = dfX_agg.set_axis(groupByCols, axis=1)

        self.__group_df_status = dfX_agg

    @property
    def raw_df_sliced(self):
        return self.__sliced_raw

    @property
    def raw_df_sliced_agg(self):
        return self.__sliced_agg

    @property
    def grouped_df_status(self):
        return self.__group_df_status

