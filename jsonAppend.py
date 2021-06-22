import numpy as np
import pandas as pd
import json
from pathlib import Path
from pandas.io.json import json_normalize
pd.set_option('display.max_columns', None)


temp = pd.DataFrame()



for filename in Path('Python FitBit/2019').glob('**/*heartbeat.json'):
    f= open(filename)
    data=json.load(f)
    # data1 = json_normalize(data)
    data1 = pd.read_json(filename,typ='series')
    temp = temp.append(data1, ignore_index=True)

print(temp.head(10))

writer = pd.ExcelWriter('Python FitBit/test.xlsx', engine='xlsxwriter')
#
temp.to_excel(writer, sheet_name='Sheet1')
#
writer.save()

