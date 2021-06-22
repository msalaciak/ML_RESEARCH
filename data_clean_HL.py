import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)


# cleaning data

LDH = pd.read_excel('clean_Data/HL/RES_ID_HL LDH.xlsx')
DIFF = pd.read_excel('clean_Data/HL/HL Diff_RES_ID.xlsx')
CBC = pd.read_excel('clean_Data/HL/RES_ID_HL CBC.xlsx')

print("##########  LDH   ##############")
print(LDH.head(10))
print("#########   DIFF   ############")
print(DIFF.head(10))
print("##########  CBC   ##############")
print(CBC.head(10))
print("##########  END   ##############")

# LDH
# LDH['TEST_DT']= pd.to_datetime(LDH['TEST_DT'],infer_datetime_format=True)
# LDH.rename(columns={'TEST_DT':'Test Date'}, inplace=True)
# LDH.rename(columns={'Res_ID':'ID'}, inplace=True)
# LDH.rename(columns={'RESULT':'LDHI'}, inplace=True)
# LDH = LDH[['ID','ORDER','Test Date','LDHI','DATE_OF_BIRTH','SEX','TEST_ID','CLINIC_ID','DOCTOR_ID','GROUP_TEST_ID','ZIP']]
#
# Missing = LDH[(LDH['LDHI'] == '.')]


# writer = pd.ExcelWriter('clean_Data/HL/missingldh.xlsx', engine='xlsxwriter')
# #
# Missing.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()



# DIFF

# DIFF['TEST_DT']= pd.to_datetime(DIFF['TEST_DT'],infer_datetime_format=True)
# DIFF.rename(columns={'TEST_DT':'Test Date'}, inplace=True)
# DIFF.rename(columns={'RES_ID':'ID'}, inplace=True)
#
# DIFF=DIFF.fillna('.')
# indexNames = DIFF[(DIFF['BASO#'] == '.') & (DIFF['EOS#'] == '.') & (DIFF['LYMP#'] == '.') & (DIFF['MONO#'] == '.') & (DIFF['NEUT#'] == '.')].index
# indexNames2 = DIFF[(DIFF['BASO#'] == '.') & (DIFF['EOS#'] == '.') & (DIFF['LYMP#'] == '.') & (DIFF['MONO#'] == '.') & (DIFF['NEUT#'] == '.')].ORDER
# DIFF.drop(indexNames, inplace=True)
# DIFF = DIFF.groupby('ORDER').max().reset_index()



# CBC

# CBC['TEST_DT']= pd.to_datetime(CBC['TEST_DT'],infer_datetime_format=True)
# CBC.rename(columns={'TEST_DT':'Test Date'}, inplace=True)
# CBC.rename(columns={'RES_ID':'ID'}, inplace=True)
#
#
# CBC["HCT"] = pd.to_numeric(CBC["HCT"],errors='coerce')
# CBC["HGB"] = pd.to_numeric(CBC["HGB"],errors='coerce')
# CBC["MCH"] = pd.to_numeric(CBC["MCH"],errors='coerce')
# CBC["MCHC"] = pd.to_numeric(CBC["MCHC"],errors='coerce')
# CBC["MCV"] = pd.to_numeric(CBC["MCV"],errors='coerce')
# CBC["NRBC#"] = pd.to_numeric(CBC["NRBC#"],errors='coerce')
# CBC["NRBC%"] = pd.to_numeric(CBC["NRBC%"],errors='coerce')
# CBC["PLAT"] = pd.to_numeric(CBC["PLAT"],errors='coerce')
# CBC["RDW"] = pd.to_numeric(CBC["RDW"],errors='coerce')
# CBC["WBC"] = pd.to_numeric(CBC["WBC"],errors='coerce')
#
#
# # CBC=CBC.fillna('.')
# # indexNames3 = CBC[(CBC['HCT'] == '.') & (CBC['HGB'] == '.') & (CBC['MCH'] == '.') & (CBC['MCHC'] == '.') & (CBC['MCV'] == '.') & (CBC['NRBC#'] == '.') & (CBC['NRBC%'] == '.') & (CBC['PLAT'] == '.') & (CBC['RDW'] == '.') & (CBC['WBC'] == '.')].index
# # indexNames4 = CBC[(CBC['HCT'] == '.') & (CBC['HGB'] == '.') & (CBC['MCH'] == '.') & (CBC['MCHC'] == '.') & (CBC['MCV'] == '.') & (CBC['NRBC#'] == '.') & (CBC['NRBC%'] == '.') & (CBC['PLAT'] == '.') & (CBC['RDW'] == '.') & (CBC['WBC'] == '.')].ORDER
# # CBC.drop(indexNames3, inplace=True)
# CBC = CBC.groupby('ORDER').max().reset_index()
# CBC=CBC.fillna('0')
#
# writer = pd.ExcelWriter('clean_Data/HL/HL_CBC_CLEANED.xlsx', engine='xlsxwriter')
# #
# CBC.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()




# print("##########  LDH   ##############")
# print(LDH.head(10))
# print("#########   DIFF   ############")
# print(DIFF.head(10))
# print("##########  CBC   ##############")
# print(CBC.head(10))
# print("##########  END   ##############")




# merge cbc and diff

# cbc=pd.read_excel('clean_Data/HL/HL_CBC_CLEANED.xlsx')
# diff =pd.read_excel('clean_Data/HL/HL_DIFF_CLEANED.xlsx')
#
# merged = pd.merge(cbc, diff, on='ORDER', how='inner')
# exclude = pd.merge(cbc, diff, on = 'ORDER', how = 'outer', indicator=True)





#merge cbc/diff and ldh

# cbc_diff=pd.read_excel('clean_Data/HL/HL_cbc_diff_merge_clean.xlsx')
#
#
# merged = pd.merge(cbc_diff, LDH, on='ORDER', how='inner')
# exclude = pd.merge(cbc_diff, LDH, on = 'ORDER', how = 'outer', indicator=True)
#
# exclude = exclude.query('_merge != "both"')
#
# writer = pd.ExcelWriter('clean_Data/HL/HL_cbc_diff_LDH_merge_clean.xlsx', engine='xlsxwriter')
# #
# merged.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/HL/HL_cbc_diff_LDH_merge_clean_EXCLUDE.xlsx', engine='xlsxwriter')
# #
# exclude.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()





#cleaning LDH again

ldh_clean = pd.read_excel('clean_Data/HL/HL_LDH_CLEANED.xlsx')
print(ldh_clean.shape)

ldh_clean = ldh_clean[ldh_clean.LDHI != '.']


# writer = pd.ExcelWriter('clean_Data/HL/HL_LDH_CLEANED_V2.xlsx', engine='xlsxwriter')
# #
# ldh_clean.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()


#missing patients cbc, diff, ldh


LDH = pd.read_excel('clean_Data/HL/HL_LDH_CLEANED_V2.xlsx')
DIFF = pd.read_excel('clean_Data/HL/HL_DIFF_CLEANED.xlsx')
CBC = pd.read_excel('clean_Data/HL/HL_CBC_CLEANED.xlsx')
HL= pd.read_excel('clean_Data/HL/HL_ID.xlsx')
CBC_DIFF= pd.read_excel('clean_data/HL/clean merged/HL_CBC_DIFF_FINAL.xlsx')
# #
# #
# merged = pd.merge(HL, DIFF, on='ID', how='inner',indicator=True)
#
# exclude = pd.merge(HL, DIFF, on = 'ID', how = 'outer', indicator=True)
# exclude = exclude.query('_merge != "both"')
#
# print(exclude.head(10))
#
#
#
# writer = pd.ExcelWriter('clean_Data/HL/MISSING/test.xlsx', engine='xlsxwriter')
# #
# exclude.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()

merged = pd.merge(CBC_DIFF, LDH, on='ORDER', how='inner',indicator=True)

exclude = pd.merge(CBC, DIFF, on = 'ORDER', how = 'outer', indicator=True)
exclude = exclude.query('_merge != "both"')

print(exclude.head(10))


#
# writer = pd.ExcelWriter('clean_Data/HL/clean merged/HL_CBC_DIFF_LDH_FINAL.xlsx', engine='xlsxwriter')
# #
# merged.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()





# LDH = pd.read_excel('clean_Data/HL/HL_LDH_CLEANED_V2.xlsx')
# DIFF = pd.read_excel('clean_Data/HL/HL_DIFF_CLEANED.xlsx')
# CBC = pd.read_excel('clean_Data/HL/HL_CBC_CLEANED.xlsx')
#
# merged = pd.merge(DIFF, CBC, on='ORDER', how='inner',indicator=True)
#
# exclude = pd.merge(DIFF, CBC, on = 'ORDER', how = 'outer', indicator=True)
# exclude = exclude.query('_merge != "both"')
#
# writer = pd.ExcelWriter('clean_Data/HL/MISSING/HL_DIFF_CBC.xlsx', engine='xlsxwriter')
# #
# merged.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()
#
# writer = pd.ExcelWriter('clean_Data/HL/MISSING/HL_DIFF_CBC_MISSING.xlsx', engine='xlsxwriter')
# #
# exclude.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()