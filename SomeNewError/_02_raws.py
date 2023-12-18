import sqlalchemy as sqa
import pandas as pd

class CLASS02_RAW:
    def __init__(self):
        query = 'select * from property_data '
        # engine = sqa.create_engine('sqlite:///Output_data.db')

        path='sqlite:////Users/mac/Dropbox/pythonProjects/Random/RM01/Output_data.db'
        # path = 'sqlite:///C:\\Users\\Muhammad Ahmad\\Desktop\\SomeNewError\\Output_data.db'
        engine = sqa.create_engine(path)

        df1_raw = pd.read_sql(query, engine)
        df1_raw.index.name = 'rowNum'

        df1_raw['Run_Date'] = pd.to_datetime(df1_raw['Run_Date']).dt.date
        df1_raw['Status_Date'] = pd.to_datetime(df1_raw['Status_Date']).dt.date

        df1_raw = df1_raw[df1_raw['Featured'] == '']  # KEEP ROWS ONLY WHERE FEATURED IS NULL. i.e Remove featured rows

        sortCol = ['Property_Unique_Number', 'Status_Date']
        df1_raw.sort_values(by=sortCol, ascending=True, inplace=True)
        primaryKeyList = ['Property_Unique_Number', 'Version_Number']
        df1_raw.set_index(primaryKeyList, inplace=True)

        self.__df1_raw = df1_raw


    @property
    def df2_raw(self):
        return self.__df1_raw