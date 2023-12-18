import pandas as pd
import datetime as dt
from datetime import datetime
import time

'''
NOTE- I SPENT TWO HOURS TRYING TO ADD THESE FUNCTIONS IN A CLASS
THE PROBLEM IS I AM UNABLE TO USE APPLY WHEN USED IN CLASS..
ANYWAY KEEPING THEM AS FUNCTION WORKS
'''

def fn_60_ADD_PRICE_BUCKET(serPrice):

    seriesBin = pd.cut(x=serPrice, bins=[0, 100000, 200000, 400000, 600000, 800000, 1000000, 10000000],
                       labels=['POA', '100k to 200k', '200k to 400k', '400k to 6000k',
                               '600k to 800k', '800k to 1m', '1m to 2m'])
    return seriesBin

def fn_61_ADD_LATEST_STATUS( prop_num,dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestStatus = specificDF['Property_Status'].iloc[-1]
    return latestStatus


def fn_62_ADD_LATEST_PRICE(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestPrice = specificDF['Price'].iloc[-1]
    return latestPrice

def fn_61_ADD_LATEST_STATUS( prop_num,dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestStatus = specificDF['Property_Status'].iloc[-1]
    return latestStatus


def fn_63_ADD_LATEST_STATUS_DATE(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    latestStatusDate = specificDF['Status_Date'].iloc[-1]
    return latestStatusDate


def fn_64_ADD_FIRST_DATE(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    firstDate = specificDF['Status_Date'].iloc[0]
    return firstDate

def fn_65_ADD_Total_Days(prop_num, dfGroupbyObj):
    specificDF = dfGroupbyObj.get_group(prop_num)
    status_date = specificDF['Status_Date'].iloc[0]
    status_date_str = status_date.strftime('%Y-%m-%d')
    firstDate = datetime.strptime(status_date_str, '%Y-%m-%d')
    # print(firstDate)
    current_date = datetime.now()
    number_of_days = abs((firstDate - current_date).days)
    return number_of_days
