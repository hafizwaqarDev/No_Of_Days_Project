import pandas as pd
from _50_REPLACE import CLASS_51_REPLACE_STATUS
import copy

class CLASS_6_REPORT_Delta_property:
    def __init__(self, delta_df):

        dfX = copy.deepcopy(delta_df)
        dfX['last_status'] = CLASS_51_REPLACE_STATUS(dfX['last_status']).series_updated_status
        groupByCols = ['Location', 'last_status']
        table1_df = pd.pivot_table(dfX, index=groupByCols, columns='priceBucket', values='last_price',
                                   aggfunc='count')

        table1_df.reset_index(inplace=True,drop=False)

        table1_df.index.name='sNo'



        self.__delta_df_status = table1_df
        
    @property
    def delta_df_status(self):
        return self.__delta_df_status





