import pandas as pd

pd.set_option('display.max_columns', None)
# Load dataframes from excel file into pandas
FILE_PATH = "/home/matthew/Research/ML_RESEARCH/"

biochem = pd.read_excel('/home/matthew/Research/ML_RESEARCH/phoi_ldh_dlbcl.xlsx')
progression_info = pd.read_excel(
    '/home/matthew/Research/ML_RESEARCH/clean_data/clean merged/primary-join-follow-up.xlsx')

#
# #Corrects date to proper format
biochem['OREDERED_DATE'] = pd.to_datetime(biochem['OREDERED_DATE'], infer_datetime_format=True)

# rename column
biochem.rename(columns={'OREDERED_DATE': 'Test Date'}, inplace=True)

#
#
# #make each test_id an individual column
#
biochem = biochem.pivot_table('RESULT',
                              ['ID', 'ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date'],
                              'TEST_ID', aggfunc='first')
biochem = biochem.reset_index()

print(biochem.head(10))
print(progression_info.head(10))

progression_info = progression_info[
    ['ID', 'Progression post RCHOP (yes = 1, no=0)', 'Date Prog after RCHOP for DLBCL', 'DATE_DLBCL Diagnosis',
     'Cause of Death', 'Date of last Follow-Up']]
progression_info.loc[progression_info['Cause of Death'] == "No", 'deceased'] = 0
progression_info.loc[progression_info['Cause of Death'] != "No", 'deceased'] = 1
merge = pd.merge(biochem, progression_info, on='ID', how='right')

exclude = pd.merge(merge, progression_info, on='ID', how='outer', indicator=True)
exclude = exclude.query('_merge != "both"')

relapsed = merge[merge['Progression post RCHOP (yes = 1, no=0)'] == 1]
no_relapse = merge[merge['Progression post RCHOP (yes = 1, no=0)'] == 0]

relapsed['PHOI'] = relapsed['PHOI'].astype(float)
relapsed['LDHI'] = relapsed['LDHI'].astype(float)

no_relapse['PHOI'] = no_relapse['PHOI'].astype(float)
no_relapse['LDHI'] = no_relapse['LDHI'].astype(float)

# date between diagnosis and relpace
relapsed['Time_between_relapse_test'] = relapsed['Test Date'] - relapsed['Date Prog after RCHOP for DLBCL']
relapsed['Time_between_dx_test'] = relapsed['Test Date'] - relapsed['DATE_DLBCL Diagnosis']
relapsed['Time_between_dx_last_follow_up'] = relapsed['Test Date'] - relapsed['Date of last Follow-Up']

no_relapse['Time_between_dx_test'] = no_relapse['Test Date'] - relapsed['DATE_DLBCL Diagnosis']
no_relapse['Time_between_dx_last_follow_up'] = no_relapse['Test Date'] - relapsed['Date of last Follow-Up']

relapsed_hypo = relapsed[relapsed['PHOI'] <= 0.5]
relapsed_hyper = relapsed[relapsed['PHOI'] >= 2.5]

no_relapse_hypo = no_relapse[no_relapse['PHOI'] <= 0.5]
no_relapse_hyper = no_relapse[no_relapse['PHOI'] >= 2.5]

relapsed_deceased = relapsed[relapsed['deceased'] == 1]
no_relapse_deceased = no_relapse[no_relapse['deceased'] == 1]

relapsed_hypo_deceased = relapsed_hypo[relapsed_hypo['deceased'] == 1]
no_relapse_hypo_deceased = no_relapse_hypo[no_relapse_hypo['deceased'] == 1]

print("number of patients no relapse with phoi ", no_relapse.ID.unique().size)
print("number of patients no relapse hypo ", no_relapse_hypo.ID.unique().size)
# print( "number of patients no relapse hyper " , no_relapse_hyper.ID.unique().size)
print("number of patients no relapse with phoi deceased", no_relapse_deceased.ID.unique().size)
print("number of patients no relapse hypo and deceased ", no_relapse_hypo_deceased.ID.unique().size)

print("number of patients relapse with phoi ", relapsed.ID.unique().size)
print("number of patients relapse hypo ", relapsed_hypo.ID.unique().size)
# print( "number of patients relapse hyper " , relapsed_hyper.ID.unique().size)
print("number of patients relapse with phoi deceased", relapsed_deceased.ID.unique().size)
print("number of patients relapse hypo and deceased", relapsed_hypo_deceased.ID.unique().size)

print("patient IDs relapse with phoi ", relapsed.ID.unique())

print("patient IDs no relapse with phoi ", no_relapse.ID.unique())

print("patient IDs no relapse hypo and deceased ", no_relapse_hypo_deceased.ID.unique())
print("patient IDs relapse hypo and deceased ", relapsed_hypo_deceased.ID.unique())

df = pd.DataFrame()
df['no_relapse'] = pd.Series(no_relapse_hypo.ID.unique())
df['relapse'] = pd.Series(relapsed_hypo.ID.unique())

# df.to_csv("hypo_k_ids.csv")

prog_update = pd.read_excel('/home/matthew/Research/ML_RESEARCH/DLBCL May 5 2020 for SPSS  adjusted_ID.xlsx')

# JGHID


boolean_series = prog_update.JGHID.isin(pd.Series(no_relapse.ID.unique()))

filtered_df_no_relapse = prog_update[boolean_series].reset_index()

boolean_series = prog_update.JGHID.isin(pd.Series(relapsed.ID.unique()))
filtered_df_relapse = prog_update[boolean_series].reset_index()

filtered_df_no_relapse = filtered_df_no_relapse.rename(columns={'ID': 'ATIM', 'JGHID': 'ID'})
filtered_df_relapse = filtered_df_relapse.rename(columns={'ID': 'ATIM', 'JGHID': 'ID'})

relapse_merge = pd.merge(relapsed_hypo, filtered_df_relapse, on="ID")
no_relapse_merge = pd.merge(no_relapse_hypo, filtered_df_no_relapse, on="ID")

relapse_merge.to_csv("hypo_k_relapse.csv")
no_relapse_merge.to_csv("hypo_k_no_relapse.csv")
