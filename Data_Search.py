import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import scipy.stats


#open file and save into dateframe
# df = pd.read_excel('clean_Data/clean merged/primary-join-follow-up.xlsx')



#subset only ID and progression column
# id_progression = df[['ID', 'Progression post RCHOP (yes = 1, no=0)', 'Date Prog after RCHOP for DLBCL', 'DATE_DLBCL Diagnosis']]
#
# print(id_progression.head(10))

#now only people who progressed post RCHOP
# id_progression = id_progression[id_progression['Progression post RCHOP (yes = 1, no=0)'] == 1]
#
# print(id_progression.head(10))



#merge these patient ids with blood results

# blood_results = pd.read_excel('clean_Data/clean merged/LDH_DIFF_CBC_merge_Clean_FINAL_TEST.xlsx')
# progression_blood_results = pd.merge(id_progression, blood_results, on=['ID'], how='inner')

# print(progression_blood_results.head(10))

# writer = pd.ExcelWriter('clean_Data/Yes_Progression.xlsx', engine='xlsxwriter')
# #
# id_progression.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()

#get all blood tests of relapse patients between 0 and 2 years
# df = pd.read_excel('clean_Data/relapse-non-relapse/Progression_Blood_RES_MONTH.xlsx')
# df["#_of_Years_tests_post"] = pd.to_numeric(df["#_of_Years_tests_post"],errors='coerce')

# print(df.head(10))

# df = df.loc[(df['#_of_Years_tests_post'] >= 0) & (df['#_of_Years_tests_post'] <= 24)]

# print(df.head(10))

# df1 = pd.read_excel('clean_Data/relapse-non-relapse/No_Progression_Blood_RES_MONTH.xlsx')
# df1["#_of_Years_tests_post"] = pd.to_numeric(df1["#_of_Years_tests_post"],errors='coerce')
# print(df1.head(10))
#
# df1 = df1.loc[(df1['#_of_Years_tests_post'] >= 0) & (df1['#_of_Years_tests_post'] <= 24)]
#
# print(df1.head(10))
#
# writer = pd.ExcelWriter('clean_Data/CLEAN__NON_Progression_MONTH.xlsx', engine='xlsxwriter')
# #
# df1.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()

#PLOT Y = LDHI X = DATE
relapse = pd.read_excel('clean_Data/CLEAN__Progression_MONTH.xlsx')
nonrelapse = pd.read_excel('clean_Data/CLEAN__NON_Progression_MONTH.xlsx')


print(list(relapse.columns))
print("#########################")
print(list(nonrelapse.columns))

print(relapse.dtypes)
print(nonrelapse.dtypes)

plt.figure(figsize=(15,10))
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI",estimator=None,data=relapse, legend='full',label="Relapse")
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI", estimator=None,data=nonrelapse, legend='full',label="Non-Relapse")
ax.set_ylabel('LDHI Levels')
ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
ax.set_title("No Multi-Data Aggregation")
plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
plt.legend(loc=2,prop={'size': 20})

plt.figure(figsize=(15,10))
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI",ci='sd', data=relapse, legend='full',label="Relapse")
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI", ci='sd',data=nonrelapse, legend='full',label="Non-Relapse")
ax.set_ylabel('LDHI Levels')
ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
ax.set_title("Estimation Mean, Confidence Interval Standard Deviation")
plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
plt.legend(loc=2,prop={'size': 20})

plt.figure(figsize=(15,10))
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI",estimator=np.std,ci=95, data=relapse, legend='full',label="Relapse",color="r")
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI",estimator=np.std,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
ax.set_ylabel('LDHI Levels')
ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
ax.set_title('Estimation Standard Deviation, Confidence Interval 95%')
plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
plt.legend(loc=2,prop={'size': 20})

plt.figure(figsize=(15,10))
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI",estimator=np.mean,ci=95, data=relapse, legend='full',label="Relapse",color="r")
ax = sns.lineplot(x="#_of_Years_tests_post", y="LDHI",estimator=np.mean,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
ax.set_ylabel('LDHI Levels')
ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
ax.set_title('Estimation Mean, Confidence Interval 95%')
plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
plt.legend(loc=2,prop={'size': 20})


plt.savefig('mean-ci-95.png', dpi=400)
plt.show()
#
# #LYMPH
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#",estimator=None,data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#", estimator=None,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('LYMP# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("No Multi-Data Aggregation")
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#",ci='sd', data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#", ci='sd',data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('LYMP# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("Estimation Mean, Confidence Interval Standard Deviation")
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#",estimator=np.std,ci=95, data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#",estimator=np.std,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('LYMP# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Standard Deviation, Confidence Interval 95%')
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#",estimator=np.mean,ci=95, data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="LYMP#",estimator=np.mean,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('LYMP# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Mean, Confidence Interval 95%')
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
# plt.show()
#
#
# #neut
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#",estimator=None,data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#", estimator=None,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('NEUT# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("No Multi-Data Aggregation")
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#",ci='sd', data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#", ci='sd',data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('NEUT# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("Estimation Mean, Confidence Interval Standard Deviation")
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#",estimator=np.std,ci=95, data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#",estimator=np.std,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('NEUT# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Standard Deviation, Confidence Interval 95%')
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#",estimator=np.mean,ci=95, data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="NEUT#",estimator=np.mean,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('NEUT# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Mean, Confidence Interval 95%')
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
# plt.savefig('NEUT-mean-ci-95.png', dpi=400)
# plt.show()



# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="HCT",estimator=np.mean,ci=95, data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="HCT",estimator=np.mean,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('HCT Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Mean, Confidence Interval 95%')
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
# plt.savefig('HCT-mean-ci-95.png', dpi=400)
# plt.show()
#
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="#_of_Years_tests_post", y="EOS#",estimator=np.mean,ci=95, data=relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="#_of_Years_tests_post", y="EOS#",estimator=np.mean,ci=95,data=nonrelapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('EOS# Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Mean, Confidence Interval 95%')
# # plt.axhline(y=230, c='black', linestyle='dashed', label="LDHI Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
# plt.savefig('EOS#-mean-ci-95.png', dpi=400)
# plt.show()



x =relapse['#_of_Years_tests_post']
y= relapse['LDHI']


test = relapse[['#_of_Years_tests_post', 'LDHI']].copy()

print(scipy.stats.pearsonr(x,y))

# nonrelapse = pd.read_excel('clean_Data/relapse-non-relapse/No_Progression_Blood_RES_MONTH_CLEAN.xlsx')
# nonrelapse = nonrelapse.loc[(nonrelapse['#_of_Years_tests_post'] >= 36)]
# nonrelapse = nonrelapse.drop(['ID','Unnamed: 0','DATE_DLBCL Diagnosis','#_of_Years_tests_post','Test_Date','ORDER'],axis=1)
# nonrelapse=nonrelapse.reset_index(drop=True)
#
# writer = pd.ExcelWriter('clean_Data/nan_2.xlsx', engine='xlsxwriter')
# #
# nonrelapse.to_excel(writer, sheet_name='Sheet1')
# #
# writer.save()