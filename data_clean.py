import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

# ///////// THIS SECTION IS FOR CLEANING DATA FRAMES
#
# df = pd.read_excel('clean_Data/cbc.xlsx')
#
# print(df.head(10))
#
# df['TEST_DT']= pd.to_datetime(df['TEST_DT'],infer_datetime_format=True)
#
# # df.rename(columns={'TEST_DT':'Test Date'}, inplace=True)
# # df.columns.values[0] = 'ID'
# print(df.head(10))
#
#
# #
# # print(df.head(10))
# #
# writer = pd.ExcelWriter('clean_Data/cbc-clean.xlsx', engine='xlsxwriter')
#
# df.to_excel(writer, sheet_name='Sheet1')
#
# writer.save()

# //////// THIS SECTION IS FOR MERGING DATA FRAMES

# df1 = pd.read_excel('clean_Data/clean copy/follow-up-clean.xlsx')
# df2 = pd.read_excel('clean_Data/clean copy/primary-only-dlbcl-copy.xlsx')
#
# print(df1.shape[0])
# print(df2.shape[0])
#
# df3 = pd.merge(df1, df2, on='ID', how='inner')
# print(df3.shape[0])
#
# exclude = pd.merge(df1, df2, on = 'ID', how = 'outer', indicator=True)
#
#
#
# exclude = exclude.query('_merge != "both"')
#
#
#
# print(exclude.shape[0])
#
# writer = pd.ExcelWriter('clean_Data/test1.xlsx', engine='xlsxwriter')
# #
# exclude.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()

#//////////// THIS SECTION FOR CLEANING BLANK DATA

# df = pd.read_excel('clean_Data/clean copy/cbc-clean.xlsx')
# #
# # print(df.head(20))
# #
# # df1 =df
# #
# #
# # # creating a list of blank entries , indexNames2 is organized by ORDER column so we can make exclude file, df.drop deletes from this list
# # #
# # # indexNames = df[(df['BASO#'] == '.') & (df['EOS#'] == '.') & (df['LYMP#'] == '.') & (df['MONO#'] == '.') & (df['NEUT#'] == '.')].index
# # #
# # #
# # # indexNames2 = df[(df['BASO#'] == '.') & (df['EOS#'] == '.') & (df['LYMP#'] == '.') & (df['MONO#'] == '.') & (df['NEUT#'] == '.')].ORDER
# # # df.drop(indexNames, inplace=True)
# #
# #
# #
# #
# # # print(indexNames)
# #
# # print(df.dtypes)
# #
# #
# # df["HCT"] = pd.to_numeric(df["HCT"],errors='coerce')
# # df["HGB"] = pd.to_numeric(df["HGB"],errors='coerce')
# # df["MCH"] = pd.to_numeric(df["MCH"],errors='coerce')
# # df["MCHC"] = pd.to_numeric(df["MCHC"],errors='coerce')
# # df["MCV"] = pd.to_numeric(df["MCV"],errors='coerce')
# # df["NRBC#"] = pd.to_numeric(df["NRBC#"],errors='coerce')
# # df["NRBC%"] = pd.to_numeric(df["NRBC%"],errors='coerce')
# # df["PLAT"] = pd.to_numeric(df["PLAT"],errors='coerce')
# # df["RDW"] = pd.to_numeric(df["RDW"],errors='coerce')
# # df["WBC"] = pd.to_numeric(df["WBC"],errors='coerce')
# #
# #
# #
# # print(df.dtypes)
# #
# # df = df.groupby('ORDER').max().reset_index()
# #
# # df9 =  df.fillna('.')
# #
# # print(df9.head(10))
# #
# # # creating a list of blank entries , indexNames2 is organized by ORDER column so we can make exclude file, df.drop deletes from this list
# # #
# # indexNames = df9[(df9['HCT'] == '.') & (df9['HGB'] == '.') & (df9['MCH'] == '.') & (df9['MCHC'] == '.') & (df9['MCV'] == '.') & (df9['NRBC#'] == '.') & (df9['NRBC%'] == '.') & (df9['PLAT'] == '.') & (df9['RDW'] == '.') & (df9['WBC'] == '.')].index
# #
# # indexNames2 = df9[(df9['HCT'] == '.') & (df9['HGB'] == '.') & (df9['MCH'] == '.') & (df9['MCHC'] == '.') & (df9['MCV'] == '.') & (df9['NRBC#'] == '.') & (df9['NRBC%'] == '.') & (df9['PLAT'] == '.') & (df9['RDW'] == '.') & (df9['WBC'] == '.')].ORDER
# #
# # df.drop(indexNames, inplace=True)
# # #
# # # # df2 = pd.DataFrame({'Index':indexNames})
# # df2 = pd.DataFrame({'ORDER' : indexNames2})
# # #
# # print(df2.head(10))
# #
# #
# #
# # writer = pd.ExcelWriter('clean_Data/cbc_clean_Merge_exclude_test.xlsx', engine='xlsxwriter')
# # #
# # df2.to_excel(writer, sheet_name='Sheet1')
# # #
# # writer.save()



#THIS SECTION FOR MERGING BLOOD TESTS ON ORDER ID

# df1 = pd.read_excel('clean_Data/clean merged/cbc_clean_Merge_test.xlsx')
# df2 = pd.read_excel('clean_Data/clean merged/diff-cleaned-merged.xlsx')
#
# print(df1.shape[0])
# print(df2.shape[0])
#
# df3 = pd.merge(df1, df2, on='ORDER', how='inner')
# print(df3.shape[0])
#
# exclude = pd.merge(df1, df2, on = 'ORDER', how = 'outer', indicator=True)
#
#
#
# exclude = exclude.query('_merge != "both"')
#
#
#
# print(exclude.shape[0])
#
# print(df3.head(5))
#
# writer = pd.ExcelWriter('clean_Data/cbc_diff_merge_clean.xlsx', engine='xlsxwriter')
# #
# df3.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()


#THIS SECTION FOR MERGING BLOOD TESTS AND LDH WITH TEST_DATE

# df1 = pd.read_excel('clean_Data/clean merged/cbc_diff_merge_clean.xlsx')
# df2 = pd.read_excel('clean_Data/clean merged/LDH_clean_Merge.xlsx')
#
# print(df1.shape[0])
# print(df2.shape[0])
#
# df3 = pd.merge(df2, df1, on= ['ID','Test_Date'], how='inner')
# print(df3.shape[0])
#
# exclude = pd.merge(df2, df1, on = ['ID','Test_Date'], how = 'outer', indicator=True)
#
#
#
# exclude = exclude.query('_merge != "both"')
#
#
#
# print(exclude.shape[0])
#
# print(df3.head(5))
#
# writer = pd.ExcelWriter('clean_Data/LDH_DIFF_CBC_merge_Clean_EXCLUDE.xlsx', engine='xlsxwriter')
# #
# exclude.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()

#//////  LDH-CBC-DIFF-MERGE fixing blank values to 0's, making sure all the datatypes are correct

# df = pd.read_excel('clean_Data/clean merged/LDH_DIFF_CBC_merge_Clean.xlsx')
#
#
# df['DATE_OF_BIRTH'] = pd.to_datetime(df['DATE_OF_BIRTH'].astype(str), format='%Y%m%d')
# print(df.loc[[14519]])
# df['LDHI'] = df['LDHI'].replace({'>':''}, regex=True)
# df["LDHI"] = pd.to_numeric(df["LDHI"],errors='coerce')
# df = df.fillna('0')
# df["HCT"] = pd.to_numeric(df["HCT"],errors='coerce')
# df["HGB"] = pd.to_numeric(df["HGB"],errors='coerce')
# df["MCH"] = pd.to_numeric(df["MCH"],errors='coerce')
# df["MCHC"] = pd.to_numeric(df["MCHC"],errors='coerce')
# df["MCV"] = pd.to_numeric(df["MCV"],errors='coerce')
# df["NRBC#"] = pd.to_numeric(df["NRBC#"],errors='coerce')
# df["NRBC%"] = pd.to_numeric(df["NRBC%"],errors='coerce')
# df["PLAT"] = pd.to_numeric(df["PLAT"],errors='coerce')
# df["RDW"] = pd.to_numeric(df["RDW"],errors='coerce')
# df["WBC"] = pd.to_numeric(df["WBC"],errors='coerce')
# df["BASO#"] = pd.to_numeric(df["BASO#"],errors='coerce')
# df["EOS#"] = pd.to_numeric(df["EOS#"],errors='coerce')
# df["LYMP#"] = pd.to_numeric(df["LYMP#"],errors='coerce')
# df["MONO#"] = pd.to_numeric(df["MONO#"],errors='coerce')
# df["NEUT#"] = pd.to_numeric(df["NEUT#"],errors='coerce')
# print(df.dtypes)
# print(df.loc[[14519]])
# df = df.sort_values(['ID','Test_Date'])
# print(df.head(10))
#
# writer = pd.ExcelWriter('clean_Data/LDH_DIFF_CBC_merge_Clean_FINAL_TEST.xlsx', engine='xlsxwriter')
# #
# df.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()

#getting confounders
#
# df= pd.read_excel('clean_Data/clean merged/primary-join-follow-up.xlsx')
# relapse = pd.read_excel('clean_Data/CLEAN__Progression_MONTH.xlsx')
# nonrelapse = pd.read_excel('clean_Data/CLEAN__NON_Progression_MONTH.xlsx')
#
#
# # nonrelapse_co = pd.merge(df,nonrelapse, on= ['ID'], how='inner')
# # nonrelapse_co = nonrelapse_co.drop_duplicates(subset='ID')
#
# relapse_co = pd.merge(df,relapse, on= ['ID'], how='inner')
# relapse_co = relapse_co.drop_duplicates(subset='ID')
#
#
#
# exclude = pd.merge(relapse_co, df, on = ['ID'], how = 'outer', indicator=True)
#
#
# exclude = exclude.query('_merge != "both"')
#
# exclude =  exclude.drop_duplicates(subset='ID')
#
#
# writer = pd.ExcelWriter('clean_Data/EXCLUDE_relapse_co.xlsx', engine='xlsxwriter')
# #
# df.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()



#Finding all the patient ID's who don't have ldhi within 10 days of diagnosis

# relapse = pd.read_excel('clean_Data/relapse-non-relapse/Yes_Progression_ID.xlsx')
# nonrelapse = pd.read_excel('clean_Data/relapse-non-relapse/No_Progression_ID.xlsx')
#
# idprog = pd.read_excel('clean_Data/ldhi_id_10day_prog.xlsx')
# idnon = pd.read_excel('clean_Data/ldhi_id_10day_nonprog.xlsx')
#
#
#
# idprog = idprog.drop_duplicates(subset='ID')
# idnon = idnon.drop_duplicates(subset='ID')



# idprog1 = pd.merge(relapse, idprog, on= ['ID'], how='inner')
# excluded_prog = pd.merge(relapse, idprog, on = ['ID'], how = 'outer', indicator=True)
# excluded_prog = excluded_prog.query('_merge != "both"')

# idnon1 = pd.merge(nonrelapse, idnon, on= ['ID'], how='inner')
# excluded_non = pd.merge(nonrelapse, idnon, on = ['ID'], how = 'outer', indicator=True)
# excluded_non = excluded_non.query('_merge != "both"')
#
# writer = pd.ExcelWriter('clean_Data/non_progression_10days_missing.xlsx', engine='xlsxwriter')
# #
# excluded_non.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()



#HL patients who we dont have cbc or ldh from


df1 = pd.read_excel('clean_Data/hl/HL_ID.xlsx')
df2 = pd.read_excel('clean_Data/data copy/RES_ID_DLBCL LDH.xlsx')

print(df1.shape[0])
print(df2.shape[0])





exclude = pd.merge(df1, df2, on = 'ID', how = 'outer', indicator=True)



exclude = exclude.query('_merge != "both"')

#
# writer = pd.ExcelWriter('clean_Data/HL_missing.xlsx', engine='xlsxwriter')
# #
# exclude.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()
