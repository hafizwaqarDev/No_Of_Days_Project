import pandas as pd
import numpy as np

class CLASS_5_REPORT_Unique_property:
    def __init__(self, unique_df):
        groupByCols = ['Location', 'last_status']
        table1_df = pd.pivot_table(unique_df, index=groupByCols, columns='priceBucket', values='last_price',
                               aggfunc='count')

      
        table1_df['Total_sum'] = table1_df.sum(axis=1)

        oldColName=pd.Series(table1_df.columns.values)
        newColName = oldColName.apply(lambda x: x+'_R')
        newColList=newColName.values.tolist()


        table1_df_ratio = table1_df.div(table1_df.iloc[:,-1], axis=0 )
        table1_df_ratio = np.round(table1_df_ratio,2)


        self.__df_list =[table1_df,table1_df_ratio]



            




    @property
    def table_1_df_list(self):
        return self.__df_list






