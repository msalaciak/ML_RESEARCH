import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

#///////// THIS SECTION IS FOR CLEANING DATA FRAMES

#Load dataframes from excel file into pandas
#
# biochem = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBCL_BIOCHEM_v2.xlsx')
# # progression_info = pd.read_excel('clean_Data/clean merged/primary-join-follow-up.xlsx')
# #
# # #Corrects date to proper format
# biochem['OREDERED_DATE']= pd.to_datetime(biochem['OREDERED_DATE'], infer_datetime_format=True)
# #
# # #rename column
# biochem.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)
# biochem.rename(columns={'RES_ID': 'ID'}, inplace=True)
# #
# #
# # #make each test_id an individual column
# #
# biochem = biochem.pivot_table('RESULT', ['ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date'], 'TEST_ID', aggfunc='first')
# biochem = biochem.reset_index()
# #
# #
# print(biochem.head(10))
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

#cleaning liver function test results.

# liver_func = pd.read_excel('clean_Data/DLBCL_BIOCHEM/DLBLC_BIOCHEM_LIVER_v1.xlsx')
# # #Corrects date to proper format
# liver_func['OREDERED_DATE']= pd.to_datetime(liver_func['OREDERED_DATE'], infer_datetime_format=True)
#
# # #rename column
# liver_func.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)
# liver_func.rename(columns={'RES_ID': 'ID'}, inplace=True)
#
# liver_func['RESULT'] = liver_func['RESULT'].str.replace('<','')
#
# print(list(liver_func.columns))
#
# # #make each test_id an individual column
# #
# liver_func = liver_func.pivot_table('RESULT', ['ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date'], 'TEST_ID', aggfunc='first')
# liver_func = liver_func.reset_index()
#
# print(liver_func.head(10))
# # # # # creating a list of blank entries , indexNames2 is organized by ORDER column so we can make exclude file, df.drop deletes from this list
# indexNames = liver_func[(liver_func['ALTI'] == '.') & (liver_func['ASTI'] == '.') & (liver_func['BILTI'] == '.')  & (liver_func['GGTI'] == '.')].index
# indexNames2 = liver_func[(liver_func['ALTI'] == '.') & (liver_func['ASTI'] == '.') & (liver_func['BILTI'] == '.')  & (liver_func['GGTI'] == '.')].ORDER_ID
# liver_func.drop(indexNames, inplace=True)
#
#
#
# print(liver_func.isnull().sum())
# liver_func = liver_func.drop(['ASTI'], axis=1)
# liver_func = liver_func.dropna()
# print(liver_func.isnull().sum())
#
#
# #load datasets that contain both crei and glucose
# both_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_BOTH_RELAPSE.xlsx')
# both_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_BOTH_NO_RELAPSE.xlsx')
#
# both_relapse.fillna(-1,inplace= True)
# both_no_relapse.fillna(-1,inplace= True)
# print(both_relapse.head(1))
#
# #merge liver dataset with crei/glucose (RELAPSE)
#
# merge_all_relapse = pd.merge(liver_func, both_relapse, on='ORDER_ID', how='inner')
#
# # #find out what was excluded from the merge
# exclude_all_relapse = pd.merge(liver_func, both_relapse, on = 'ORDER_ID', how = 'outer', indicator=True)
# exclude_all_relapse = exclude_all_relapse.query('_merge != "both"')
#
# #merge liver dataset with crei/glucose (NON-RELAPSE)
#
# merge_all_nonrelapse = pd.merge(liver_func, both_no_relapse, on='ORDER_ID', how='inner')
#
# # #find out what was excluded from the merge
# exclude_all_nonrelapse = pd.merge(liver_func, both_no_relapse, on = 'ORDER_ID', how = 'outer', indicator=True)
# exclude_all_nonrelapse = exclude_all_nonrelapse.query('_merge != "both"')
#
# #save to excel files
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/RELAPSE_MERGE_ALL.xlsx', engine='xlsxwriter')
# merge_all_relapse.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/RELAPSE_EXCLUDE_ALL.xlsx', engine='xlsxwriter')
# exclude_all_relapse.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/NONRELAPSE_MERGE_ALL.xlsx', engine='xlsxwriter')
# merge_all_nonrelapse.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/NONRELAPSE_EXCLUDE_ALL.xlsx', engine='xlsxwriter')
# exclude_all_nonrelapse.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#

# CLEANING HBA1C
##
###
####
##
#

# progression_info = pd.read_excel('clean_Data/clean merged/primary-join-follow-up.xlsx')
# print(progression_info.head(10))
#
#
# hba1c = pd.read_excel('clean_data/DLBCL_BIOCHEM/diabetes/DLBCL_HBA1C.xlsx')
# hba1c['OREDERED_DATE']= pd.to_datetime(hba1c['OREDERED_DATE'], infer_datetime_format=True)
# hba1c.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)
# hba1c.rename(columns={'RES_ID': 'ID'}, inplace=True)
# print(list(hba1c.columns))
#
# hba1c = hba1c.pivot_table('RESULT', ['ID', 'ORDER_ID', 'GROUP_TEST_ID','CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date', 'TEST_NAME'], 'TEST_ID', aggfunc='first')
# hba1c = hba1c.reset_index()
#
#
# print(hba1c.head(10))
#
# print(list(hba1c.columns))
#
# merge = pd.merge(hba1c, progression_info, on='ID', how='inner')
#
# # #find out what was excluded from the merge
# exclude = pd.merge(hba1c, progression_info, on = 'ID', how = 'outer', indicator=True)
# exclude = exclude.query('_merge != "both"')
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/diabetes/merged_hba1c_prog_info.xlsx', engine='xlsxwriter')
# merge.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/diabetes/excluded_hba1c_prog_info.xlsx', engine='xlsxwriter')
# exclude.to_excel(writer, sheet_name='Sheet1')
# writer.save()


# SODIUM AL CAL CLEANING


# biochem = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem_cal_al_sod.xlsx')
#
# #
# # #Corrects date to proper format
# biochem['OREDERED_DATE']= pd.to_datetime(biochem['OREDERED_DATE'], infer_datetime_format=True)
# #
# # #rename column
# biochem.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)
# biochem.rename(columns={'RES_ID': 'ID'}, inplace=True)
# #
# #
# # #make each test_id an individual column
# #
# biochem = biochem.pivot_table('RESULT', ['ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date'], 'TEST_NAME', aggfunc='first')
# biochem = biochem.reset_index()
# #
#
# print(biochem.head(10))
# print(biochem.shape)
#
# # dropping blank entries
# indexNames = biochem[(biochem['Albumin'] == '.') & (biochem['Calcium'] == '.') & (biochem['Sodium'] == '.')].index
# indexNames2 = biochem[(biochem['Albumin'] == '.') & (biochem['Calcium'] == '.') & (biochem['Sodium'] == '.')].ORDER_ID
# biochem.drop(indexNames, inplace=True)
# print(biochem.head(10))
# print(biochem.shape)
#
# biochem["Albumin"] = pd.to_numeric(biochem["Albumin"], errors='coerce')
# biochem["Calcium"] = pd.to_numeric(biochem["Calcium"], errors='coerce')
# biochem["Sodium"] = pd.to_numeric(biochem["Sodium"], errors='coerce')
#
# biochem = biochem.dropna()
# biochem = biochem.reset_index()
# print(biochem.head(10))
# print(biochem.shape)
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/sod-al-cal-cleaned.xlsx', engine='xlsxwriter')
# biochem.to_excel(writer, sheet_name='Sheet1')
# writer.save()


# quick script to check missing entries for chemo / weight start dates.
relapse = pd.read_excel('clean_data/CLEAN_Progression.xlsx')
nonrelapse = pd.read_excel('clean_data/CLEAN__NON_Progression.xlsx')
chemo = pd.read_excel('RES_ID_DLBCL_IPI_chemodates.xlsx')




# excludeProg = pd.merge(relapse, chemo, on = 'ID', how = 'outer', indicator=True)
# excludeProg = excludeProg.query('_merge != "both"')
#
# excludeNON = pd.merge(nonrelapse, chemo, on = 'ID', how = 'outer', indicator=True)
# excludeNON = excludeNON.query('_merge != "both"')

# excludeNON = nonrelapse.merge(chemo, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
# excludeProg = relapse.merge(chemo, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
#
#
# excludeNON = excludeNON['ID']
# excludeProg = excludeProg['ID']
#
#
# excludeNON = excludeNON.drop_duplicates()
# excludeProg = excludeProg.drop_duplicates()
#
#
#
# writer = pd.ExcelWriter('clean_Data/chemo_dates_missing_prog.xlsx', engine='xlsxwriter')
# excludeProg.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/chemo_dates_missing_non.xlsx', engine='xlsxwriter')
# excludeNON.to_excel(writer, sheet_name='Sheet1')
# writer.save()


#CHEM H CLEANING
# chemh = pd.read_excel('clean_data/DLBCL_BIOCHEM/chem_h_only.xlsx')
# glucose_filled = pd.read_excel('clean_data/gluc_stats_filled.xlsx')
#
#
# print(chemh.head(10))
#
# chemh = chemh.pivot_table('RESULT', ['RES_ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'OREDERED_DATE'], 'TEST_ID', aggfunc='first')
# chemh = chemh.reset_index()
#
# print(chemh.head(10))
#
#
#
# join = pd.merge(chemh,glucose_filled,on=['RES_ID','ORDER_ID'])
#
# writer = pd.ExcelWriter('clean_Data/chemh_full_tests.xlsx', engine='xlsxwriter')
# join.to_excel(writer, sheet_name='Sheet1')
# writer.save()

chemh = pd.read_excel('clean_data/chemh_full_tests_clean.xlsx')
print(chemh.head(10))
chemh['OREDERED_DATE']= pd.to_datetime(chemh['OREDERED_DATE'], infer_datetime_format=True)
print(chemh.head(10))

writer = pd.ExcelWriter('clean_Data/chemh_full_tests_clean.xlsx', engine='xlsxwriter')
chemh.to_excel(writer, sheet_name='Sheet1')
writer.save()