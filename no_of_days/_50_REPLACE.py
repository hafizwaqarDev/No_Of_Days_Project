import pandas as pd

class CLASS_51_REPLACE_STATUS:
    def __init__(self,seriesLatestStatus):

        replaceDict = {
            'UNDER OFFER': 'SOLD',
            'SOLD STC': 'SOLD'

        }

        self.series_updated_status = seriesLatestStatus.replace(replaceDict)

class CLASS_52_REPLACE_TYPE:
    def __init__(self, seriesLatesttype):

        replaceDict = {
            'End of Terrace': 'Terraced',
            'Link Detached House': 'Detached',
            'Town House': 'Terraced'
        }
        self.series_updated_type = seriesLatesttype.replace(replaceDict)


