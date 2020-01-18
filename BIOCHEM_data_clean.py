import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#///////// THIS SECTION IS FOR CLEANING DATA FRAMES

#Load dataframes from excel file into pandas

df = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_v2.xlsx')
print(df.head(10))

#Corrects date to proper format
df['OREDERED_DATE']= pd.to_datetime(df['OREDERED_DATE'],infer_datetime_format=True)

#rename column
df.rename(columns={'OREDERED_DATE':'Test Date'}, inplace=True)


#make each test_id an individual column
df = df.pivot(columns='TEST_ID', values='RESULT')

print(df.head(10))

#save to new excel.
writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_v2_test.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

writer.save()