import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
pd.set_option('display.max_columns', None)
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

from sklearn.decomposition import PCA

from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.metrics import confusion_matrix

from sklearn.tree import export_graphviz
import random


#load datasets that contain blood test results
relapse = pd.read_excel('clean_Data/relapse-non-relapse/Progression_Blood_RES_DAY_CLEAN.xlsx')
nonrelapse = pd.read_excel('clean_Data/relapse-non-relapse/No_Progression_Blood_RES_MONTH_CLEAN.xlsx')

#filter out the blood test date results. relapse is 28 days prior to relapse date, non relapse is 28 months of test results
nonrelapse = nonrelapse.loc[(nonrelapse['#_of_Years_tests_post'] >= 24)]
relapse.loc[(relapse['#_of_Years_tests_post'] >= 0) & (relapse['#_of_Years_tests_post'] <= 28)]




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
glucose_relapse = glucose_relapse.loc[(glucose_relapse['tests months diagnosis'] >= 0) & (glucose_relapse['tests weeks prior relapse'] <= 28)]
glucose_no_relapse = glucose_no_relapse.loc[(glucose_no_relapse['tests months diagnosis'] >= 24)]
crei_relapse = crei_relapse.loc[(crei_relapse['tests months diagnosis'] >= 0) & (crei_relapse['tests weeks prior relapse'] <= 28)]
crei_no_relapse = crei_no_relapse.loc[(crei_no_relapse['tests months diagnosis'] >= 24)]

print(print(list(nonrelapse.columns)))
print(print(list(glucose_relapse.columns)))



# #merging datasets together (First we need to rename test date so it matches in both

glucose_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
glucose_no_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
crei_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
crei_no_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)

glucose_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
glucose_no_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
crei_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
crei_no_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)







relapse = pd.merge(relapse, glucose_relapse, on=['ORDER'], how='inner')

# # #find out what was excluded from the merge
exclude_Relapse = pd.merge(relapse, glucose_relapse, on = ['ORDER'], how = 'outer', indicator=True)
exclude_Relapse = exclude_Relapse.query('_merge != "both"')

nonrelapse = pd.merge(nonrelapse, glucose_no_relapse, on=['ORDER'], how='inner')

# # #find out what was excluded from the merge
exclude_nonRelapse = pd.merge(nonrelapse, glucose_no_relapse, on = ['ORDER'], how = 'outer', indicator=True)
exclude_nonRelapse = exclude_nonRelapse.query('_merge != "both"')

writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/MASTER_RELAPSE_MERGE.xlsx', engine='xlsxwriter')
relapse.to_excel(writer, sheet_name='Sheet1')
writer.save()
#
writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/MASTER_NONRELAPSE_MERGE.xlsx', engine='xlsxwriter')
nonrelapse.to_excel(writer, sheet_name='Sheet1')
writer.save()
