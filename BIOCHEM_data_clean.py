import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#///////// THIS SECTION IS FOR CLEANING DATA FRAMES

#Load dataframes from excel file into pandas

biochem = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_v2.xlsx')
progression_info = pd.read_excel('clean_Data/clean merged/primary-join-follow-up.xlsx')

#Corrects date to proper format
biochem['OREDERED_DATE']= pd.to_datetime(biochem['OREDERED_DATE'], infer_datetime_format=True)

#rename column
biochem.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)
biochem.rename(columns={'RES_ID': 'ID'}, inplace=True)


#make each test_id an individual column

biochem = biochem.pivot_table('RESULT', ['ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date'], 'TEST_ID', aggfunc='first')
biochem = biochem.reset_index()


# print(df.head(10))

# # # creating a list of blank entries , indexNames2 is organized by ORDER column so we can make exclude file, df.drop deletes from this list
indexNames = biochem[(biochem['CREI'] == '.') & (biochem['GLUI'] == '.') & (biochem['GLUII'] == '.')].index
indexNames2 = biochem[(biochem['CREI'] == '.') & (biochem['GLUI'] == '.') & (biochem['GLUII'] == '.')].ORDER_ID
biochem.drop(indexNames, inplace=True)

#Convert GLUI,CREI,GLUII to floats
biochem["CREI"] = pd.to_numeric(biochem["CREI"], errors='coerce')
biochem["GLUI"] = pd.to_numeric(biochem["GLUI"], errors='coerce')
biochem["GLUII"] = pd.to_numeric(biochem["GLUII"], errors='coerce')
print(biochem.dtypes)

#create a new column that consists of the larger of the two values from GLUI and GLUII
biochem["GLUCOSE"] = np.nanmax(biochem[["GLUI", "GLUII"]].values, axis=1)



print(biochem.head(10))

progression_info = progression_info[['ID', 'Progression post RCHOP (yes = 1, no=0)', 'Date Prog after RCHOP for DLBCL', 'DATE_DLBCL Diagnosis']]

merge = pd.merge(biochem, progression_info, on='ID', how='inner')

print(merge.head(10))

exclude = pd.merge(merge, progression_info, on = 'ID', how = 'outer', indicator=True)

exclude = exclude.query('_merge != "both"')

print("EXCLUDED")
print(exclude.head(10))


# save to new excel.
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_v2_clean_3.xlsx', engine='xlsxwriter')
#
# biochem.to_excel(writer, sheet_name='Sheet1')
#
# writer.save()

