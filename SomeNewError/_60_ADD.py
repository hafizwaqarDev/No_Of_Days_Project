import pandas as pd
import datetime as dt
from datetime import datetime
import datetime
import time
import pandas._libs.tslibs.timestamps
'''
NOTE- I SPENT TWO HOURS TRYING TO ADD THESE FUNCTIONS IN A CLASS
THE PROBLEM IS I AM UNABLE TO USE APPLY WHEN USED IN CLASS..
ANYWAY KEEPING THEM AS FUNCTION WORKS
'''

def fn_60_ADD_PRICE_BUCKET(serPrice):
    seriesBin = pd.cut(x=serPrice, bins=[0, 100000, 200000, 400000,600000, 700000, 800000,900000,  1000000, 10000000],
                       labels=['POA', '100k to 200k', '200k to 400k', '400k to 600k',
                               '600k to 700k', '700k to 800k','800k to 900k', '900k to 1m','1m to 2m'])
    return seriesBin

def fn_61_ADD_LATEST_STATUS( prop_num,dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestStatus = specificDF['Property_Status'].iloc[-1]
    return latestStatus


def fn_62_ADD_LATEST_PRICE(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestPrice = specificDF['Price'].iloc[-1]
    return latestPrice


def fn_63_ADD_LATEST_STATUS_DATE(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestStatusDate = specificDF['Status_Date'].iloc[-1]
    return latestStatusDate


def fn_64_ADD_FIRST_DATE(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    firstDate = specificDF['Status_Date'].iloc[0]
    return firstDate

def fn_65_ADD_Total_Days(prop_num, dfGroupbyObj):
    from datetime import datetime
    specificDF = dfGroupbyObj.get_group(prop_num)
    status_date = specificDF['Status_Date'].iloc[0]
    status_date_str = status_date.strftime('%Y-%m-%d')
    firstDate = datetime.strptime(status_date_str, '%Y-%m-%d')
    current_date = datetime.now()
    number_of_days = abs((firstDate - current_date).days)
    print(number_of_days)
    return number_of_days

def fn_66_SAME_DATE_SOLD(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    row, col = specificDF.shape
    if row == 2:
        firstStatusDateTag = specificDF['Status_Date'].iloc[0]
        first_status_date_str = firstStatusDateTag.strftime('%Y-%m-%d')
        firstStatusDate = datetime.strptime(first_status_date_str, '%Y-%m-%d')
        firstStatus = specificDF['Property_Status'].iloc[0]
        
        lastStatusDateTag = specificDF['Status_Date'].iloc[-1]
        last_status_date_str = lastStatusDateTag.strftime('%Y-%m-%d')
        lastStatusDate = datetime.strptime(last_status_date_str, '%Y-%m-%d')
        lastStatus = specificDF['Property_Status'].iloc[-1]
        
        firstType = type(firstStatusDate)
        lastType = type(lastStatusDate)
        delta = lastStatusDate - firstStatusDate

        print ('prop_num: ',prop_num,'firstType: ',firstType,'lastType: ',lastType)

        '''convert it to DateTimeobject if its not a datetime object here '''

  




        cond1 = firstStatus =='Initial entry'
        cond2 =  lastStatus== 'SOLD STC' or lastStatus =='UNDER OFFER'
        cond3 = firstStatusDate == lastStatusDate

        if cond1 and cond2 and cond3:
            val=1
        else:
            val=0

    else:
        val=0

    return val