import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#///////// THIS SECTION IS FOR CLEANING DATA FRAMES

#Load dataframes from excel file into pandas

# biochem = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_v2.xlsx')
# progression_info = pd.read_excel('clean_Data/clean merged/primary-join-follow-up.xlsx')
#
# #Corrects date to proper format
# biochem['OREDERED_DATE']= pd.to_datetime(biochem['OREDERED_DATE'], infer_datetime_format=True)
#
# #rename column
# biochem.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)
# biochem.rename(columns={'RES_ID': 'ID'}, inplace=True)
#
#
# #make each test_id an individual column
#
# biochem = biochem.pivot_table('RESULT', ['ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date'], 'TEST_ID', aggfunc='first')
# biochem = biochem.reset_index()
#
#
# # print(df.head(10))
#
# # # # creating a list of blank entries , indexNames2 is organized by ORDER column so we can make exclude file, df.drop deletes from this list
# indexNames = biochem[(biochem['CREI'] == '.') & (biochem['GLUI'] == '.') & (biochem['GLUII'] == '.')].index
# indexNames2 = biochem[(biochem['CREI'] == '.') & (biochem['GLUI'] == '.') & (biochem['GLUII'] == '.')].ORDER_ID
# biochem.drop(indexNames, inplace=True)
#
# #Convert GLUI,CREI,GLUII to floats
# biochem["CREI"] = pd.to_numeric(biochem["CREI"], errors='coerce')
# biochem["GLUI"] = pd.to_numeric(biochem["GLUI"], errors='coerce')
# biochem["GLUII"] = pd.to_numeric(biochem["GLUII"], errors='coerce')
# print(biochem.dtypes)
#
# #create a new column that consists of the larger of the two values from GLUI and GLUII
# biochem["GLUCOSE"] = np.nanmax(biochem[["GLUI", "GLUII"]].values, axis=1)
#
# #merge progression info and biochem datasets
# progression_info = progression_info[['ID', 'Progression post RCHOP (yes = 1, no=0)', 'Date Prog after RCHOP for DLBCL', 'DATE_DLBCL Diagnosis']]
# merge = pd.merge(biochem, progression_info, on='ID', how='inner')
#
# #find out what was excluded from the merge
# exclude = pd.merge(merge, progression_info, on = 'ID', how = 'outer', indicator=True)
# exclude = exclude.query('_merge != "both"')


# save to new excel.
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_prog_merge.xlsx', engine='xlsxwriter')
# merge.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_prog_exclude.xlsx', engine='xlsxwriter')
# exclude.to_excel(writer, sheet_name='Sheet1')
# writer.save()


# #reload merged datasets and lets remove blank entries
# glucose = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_prog_merge.xlsx')
# crei = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_CREI_prog_merge.xlsx')
# both = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_CREI_prog_merge.xlsx')
#
# #find the size before deleting blank entries so we know how many we removed from each
# print("Glucose size before")
# print(glucose.shape)
# print("Crei size before")
# print(crei.shape)
# print("combined size before")
# print(both.shape)
#
# #saving columns that have missing entries so we can see if we can find them later on
# glucose_NA = glucose.loc[pd.isnull(glucose[['GLUCOSE']]).any(axis=1)]
# crei_NA = crei.loc[pd.isnull(crei[['CREI']]).any(axis=1)]
# both_NA = both.loc[pd.isnull(both[['GLUCOSE', 'CREI']]).any(axis=1)]
#
#
#
#
# #dropping blanks in known columns (glucose / crei)
# glucose = glucose.dropna(subset=['GLUCOSE'])
# crei = crei.dropna(subset=['CREI'])
# both = both.dropna(subset=['GLUCOSE', 'CREI'])
#
# #double checking we didnt drop date prog after rchop for non relapse patients
# print(glucose.columns[glucose.isna().any()].tolist())
# print(crei.columns[crei.isna().any()].tolist())
# print(both.columns[both.isna().any()].tolist())
#
# #find the size after deleting blank entries so we know how many we removed from each
# print("Glucose size before")
# print(glucose.shape)
# print("Crei size before")
# print(crei.shape)
# print("combined size before")
# print(both.shape)
#
#
# # save to new excel.
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_prog_merge.xlsx', engine='xlsxwriter')
# glucose.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_CREI_prog_merge.xlsx', engine='xlsxwriter')
# crei.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_CREI_prog_merge.xlsx', engine='xlsxwriter')
# both.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_GLUCOSE_NAN.xlsx', engine='xlsxwriter')
# glucose_NA.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_CREI_NAN.xlsx', engine='xlsxwriter')
# crei_NA.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_BOTH_NAN.xlsx', engine='xlsxwriter')
# both_NA.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#

