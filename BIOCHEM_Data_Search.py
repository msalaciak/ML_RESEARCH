import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import scipy.stats

#bringing in the dataframes we will use
glucose_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_GLUCOSE_RELAPSE.xlsx')
glucose_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_GLUCOSE_NO_RELAPSE.xlsx')
crei_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_CREI_RELAPSE.xlsx')
crei_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_CREI_NO_RELAPSE.xlsx')

#in our datasets, we calculated the time between test date and diagnosis/relapse.
#sometimes the number is negative, so we will replace them all with a uniformed value such as -1 so we can filter it out later if needed.

glucose_relapse.fillna(-1,inplace= True)
glucose_no_relapse.fillna(-1,inplace=True)
crei_relapse.fillna(-1,inplace=True)
crei_no_relapse.fillna(-1,inplace=True)


#only looking at the data that shows test results between 0 and 24 months of diagnosis
glucose_relapse = glucose_relapse.loc[(glucose_relapse['tests months diagnosis'] >= 0) & (glucose_relapse['tests months diagnosis'] <= 24)]
glucose_no_relapse = glucose_no_relapse.loc[(glucose_no_relapse['tests months diagnosis'] >= 0) & (glucose_no_relapse['tests months diagnosis'] <= 24)]
crei_relapse = crei_relapse.loc[(crei_relapse['tests months diagnosis'] >= 0) & (crei_relapse['tests months diagnosis'] <= 24)]
crei_no_relapse = crei_no_relapse.loc[(crei_no_relapse['tests months diagnosis'] >= 0) & (crei_no_relapse['tests months diagnosis'] <= 24)]


#Patient ID's that have DM2 mentioned plus for loop to drop them from both cohorts

# ID_drop = [100699,141895,260090,292168,318224,357677,398963,628223,642729,971930
# ,1071523
# ,1072203
# ,1124009
# ,1134912
# ,1161752
# ,1382755
# ,1392776]

#removing these patients from the peak
ID_drop=  [202862,292168,318224,353974,357677,358598,398963,951650,972548,1134912,1382755,1392776]

# for x in ID_drop:
#     print("Xtzrt")
#     glucose_no_relapse = glucose_no_relapse[glucose_no_relapse.ID != x]
#     glucose_relapse = glucose_relapse[glucose_relapse.ID !=x]
#
#     print("done")

glucose_no_relapse = glucose_no_relapse[~glucose_no_relapse.ID.isin(ID_drop)]
glucose_relapse = glucose_relapse[~glucose_relapse.ID.isin(ID_drop)]

print("Exit")


#plotting bloodtests over 24 months vs gluclose levels in both cohorts

#glucose
#
# plt.figure(figsize=(15,10))
# # plt.xticks(range(0, 25))
# ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE",estimator=None,data=glucose_relapse, legend='full',label="Relapse")
# ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE", estimator=None,data=glucose_no_relapse, legend='full',label="Non-Relapse")
# ax.set_ylabel('Glucose Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("No Multi-Data Aggregation")
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE",ci='sd', data=glucose_relapse, legend='full',label="Relapse")
# ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE", ci='sd',data=glucose_no_relapse, legend='full',label="Non-Relapse")
# ax.set_ylabel('Glucose Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("Estimation Mean, Confidence Interval Standard Deviation")
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE",estimator=np.std,ci=95, data=glucose_relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE",estimator=np.std,ci=95,data=glucose_no_relapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('Glucose Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Standard Deviation, Confidence Interval 95%')
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})

plt.figure(figsize=(15,10))
plt.xticks(range(0, 120))
ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE",estimator=np.mean,ci=95, data=glucose_relapse, legend='full',label="Relapse",color="r")
ax = sns.lineplot(x="tests months diagnosis", y="GLUCOSE",estimator=np.mean,ci=95,data=glucose_no_relapse, legend='full',label="Non-Relapse",color="b")
ax.set_ylabel('Glucose Levels')
ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
ax.set_title('Estimation Mean, Confidence Interval 95%')
plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
plt.legend(loc=2,prop={'size': 20})


# plt.savefig('GLUCOSE-PLOT.png', dpi=400)
plt.show()


#Creatinine
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="tests months diagnosis", y="CREI",estimator=None,data=crei_relapse, legend='full',label="Relapse")
# ax = sns.lineplot(x="tests months diagnosis", y="CREI", estimator=None,data=crei_no_relapse, legend='full',label="Non-Relapse")
# ax.set_ylabel('Creatinine Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("No Multi-Data Aggregation")
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="tests months diagnosis", y="CREI",ci='sd', data=crei_relapse, legend='full',label="Relapse")
# ax = sns.lineplot(x="tests months diagnosis", y="CREI", ci='sd',data=crei_no_relapse, legend='full',label="Non-Relapse")
# ax.set_ylabel('Creatinine Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title("Estimation Mean, Confidence Interval Standard Deviation")
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="tests months diagnosis", y="CREI",estimator=np.std,ci=95, data=crei_relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="tests months diagnosis", y="CREI",estimator=np.std,ci=95,data=crei_no_relapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('Creatinine Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Standard Deviation, Confidence Interval 95%')
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
# plt.figure(figsize=(15,10))
# ax = sns.lineplot(x="tests months diagnosis", y="CREI",estimator=np.mean,ci=95, data=crei_relapse, legend='full',label="Relapse",color="r")
# ax = sns.lineplot(x="tests months diagnosis", y="CREI",estimator=np.mean,ci=95,data=crei_no_relapse, legend='full',label="Non-Relapse",color="b")
# ax.set_ylabel('Creatinine Levels')
# ax.set_xlabel('Blood Test Results Over 24 Months From Initial Diagnosis')
# ax.set_title('Estimation Mean, Confidence Interval 95%')
# plt.axhline(y=11, c='black', linestyle='dashed', label="Glucose Normal Value Limit")
# plt.legend(loc=2,prop={'size': 20})
#
#
# plt.savefig('Creatinine-PLOT.png', dpi=400)
# plt.show()

