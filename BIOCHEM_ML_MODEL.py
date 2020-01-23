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
import random
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedShuffleSplit


# #load datasets that contain blood test results
# relapse = pd.read_excel('clean_Data/relapse-non-relapse/Progression_Blood_RES_DAY_CLEAN.xlsx')
# nonrelapse = pd.read_excel('clean_Data/relapse-non-relapse/No_Progression_Blood_RES_MONTH_CLEAN.xlsx')
#
# #filter out the blood test date results. relapse is 28 days prior to relapse date, non relapse is 28 months of test results
# nonrelapse = nonrelapse.loc[(nonrelapse['#_of_Years_tests_post'] >= 24)]
# relapse.loc[(relapse['#_of_Years_tests_post'] >= 0) & (relapse['#_of_Years_tests_post'] <= 28)]
#
#
#
#
# #bringing in the dataframes we will use
# glucose_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_GLUCOSE_RELAPSE.xlsx')
# glucose_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_GLUCOSE_NO_RELAPSE.xlsx')
# crei_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_CREI_RELAPSE.xlsx')
# crei_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/biochem relapse - no relapse/DLBCL_BIOCHEM_CREI_NO_RELAPSE.xlsx')
#
# #in our datasets, we calculated the time between test date and diagnosis/relapse.
# #sometimes the number is negative, so we will replace them all with a uniformed value such as -1 so we can filter it out later if needed.
#
# glucose_relapse.fillna(-1,inplace= True)
# glucose_no_relapse.fillna(-1,inplace=True)
# crei_relapse.fillna(-1,inplace=True)
# crei_no_relapse.fillna(-1,inplace=True)
#
#
# #only looking at the data that shows test results between 0 and 24 months of diagnosis
# glucose_relapse = glucose_relapse.loc[(glucose_relapse['tests weeks prior relapse'] >= 0) & (glucose_relapse['tests weeks prior relapse'] <= 28)]
# glucose_no_relapse = glucose_no_relapse.loc[(glucose_no_relapse['tests months diagnosis'] >= 24)]
# crei_relapse = crei_relapse.loc[(crei_relapse['tests weeks prior relapse'] >= 0) & (crei_relapse['tests weeks prior relapse'] <= 28)]
# crei_no_relapse = crei_no_relapse.loc[(crei_no_relapse['tests months diagnosis'] >= 24)]
#
# print(print(list(nonrelapse.columns)))
# print(print(list(glucose_relapse.columns)))
#
#
#
# # #merging datasets together (First we need to rename test date so it matches in both
#
# glucose_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
# glucose_no_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
# crei_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
# crei_no_relapse.rename(columns={'Test Date': 'Test_Date'}, inplace=True)
#
# glucose_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
# glucose_no_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
# crei_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
# crei_no_relapse.rename(columns={'ORDER_ID': 'ORDER'}, inplace=True)
#
#
#
#
#
#
#
# relapse = pd.merge(relapse, glucose_relapse, on=['ORDER'], how='inner')
#
# # # #find out what was excluded from the merge
# exclude_Relapse = pd.merge(relapse, glucose_relapse, on = ['ORDER'], how = 'outer', indicator=True)
# exclude_Relapse = exclude_Relapse.query('_merge != "both"')
#
# nonrelapse = pd.merge(nonrelapse, glucose_no_relapse, on=['ORDER'], how='inner')
#
# # # #find out what was excluded from the merge
# exclude_nonRelapse = pd.merge(nonrelapse, glucose_no_relapse, on = ['ORDER'], how = 'outer', indicator=True)
# exclude_nonRelapse = exclude_nonRelapse.query('_merge != "both"')
#
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/MASTER_RELAPSE_MERGE.xlsx', engine='xlsxwriter')
# relapse.to_excel(writer, sheet_name='Sheet1')
# writer.save()
# #
# writer = pd.ExcelWriter('clean_Data/DLBCL_BIOCHEM/MASTER_NONRELAPSE_MERGE.xlsx', engine='xlsxwriter')
# nonrelapse.to_excel(writer, sheet_name='Sheet1')
# writer.save()

#////////////////////////////////////////
#///////////////////////////////////////
#
# #load datasets (blood / crei / glucose)
both_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/MASTER_RELAPSE_MERGE.xlsx')
both_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/MASTER_NONRELAPSE_MERGE.xlsx')

relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/RELAPSE_MERGE_ALL.xlsx')
no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/NONRELAPSE_MERGE_ALL.xlsx')

both_relapse = both_relapse.loc[(both_relapse['tests weeks prior relapse'] >= 0) & (both_relapse['tests weeks prior relapse'] <= 56)]
both_no_relapse = both_no_relapse.loc[(both_no_relapse['tests months diagnosis'] >= 24)]

relapse = relapse.loc[(relapse['tests weeks prior relapse'] >= 0) & (both_relapse['tests weeks prior relapse'] <= 56)]
no_relapse = no_relapse.loc[(no_relapse['tests months diagnosis'] >= 24)]

both_relapse =  pd.merge(both_relapse, relapse, on=['ORDER'], how='inner')
both_no_relapse = pd.merge(both_no_relapse,no_relapse, on=['ORDER'],how='inner')

print(list(both_relapse.columns))
print(list(both_no_relapse.columns))


#drop columns we dont need in our model
both_relapse = both_relapse.drop(['Unnamed: 0_x', 'Unnamed: 0_x', 'ID_x_x', '#_of_Years_tests_post', 'Test_Date_x', 'ORDER',  'Unnamed: 0_y', 'ID_y_x', 'CLINIC_ID_x_x', 'DOCTOR_ID_x_x', 'ORDERING_WORKSTATION_ID_x_x', 'Test_Date_y', 'GLUCOSE_x',  'Date Prog after RCHOP for DLBCL_y', 'DATE_DLBCL Diagnosis_x', 'tests months diagnosis_x', 'tests weeks prior relapse_x', 'Unnamed: 0.1_x', 'ID', 'CLINIC_ID_y_x', 'DOCTOR_ID_y_x', 'ORDERING_WORKSTATION_ID_y_x', 'Test_Date', 'CREI_x', 'Date Prog after RCHOP for DLBCL_x', 'DATE_DLBCL Diagnosis_y', 'tests months diagnosis_y', 'tests weeks prior relapse_x', 'Unnamed: 0_y', 'ID_x_y', 'CLINIC_ID_x_y', 'DOCTOR_ID_x_y', 'ORDERING_WORKSTATION_ID_x_y', 'Test Date_x', 'Unnamed: 0.1_y', 'ID_y_y', 'CLINIC_ID_y_y', 'DOCTOR_ID_y_y', 'ORDERING_WORKSTATION_ID_y_y', 'Test Date_y', 'Progression post RCHOP (yes = 1, no=0)_y', 'Date Prog after RCHOP for DLBCL_y', 'DATE_DLBCL Diagnosis', 'tests months diagnosis', 'tests weeks prior relapse_y']
,axis=1)

both_no_relapse = both_no_relapse.drop(['Unnamed: 0_x', 'Unnamed: 0_x', 'ID_x_x', 'DATE_DLBCL Diagnosis_x', 'Test_Date_x', '#_of_Years_tests_post', 'ORDER', 'Unnamed: 0_y', 'ID_y_x', 'CLINIC_ID_x_x', 'DOCTOR_ID_x_x', 'ORDERING_WORKSTATION_ID_x_x', 'Test_Date_y', 'GLUCOSE_x', 'DATE_DLBCL Diagnosis_y', 'tests months diagnosis_x', 'Unnamed: 0.1_x', 'ID', 'CLINIC_ID_y_x', 'DOCTOR_ID_y_x', 'ORDERING_WORKSTATION_ID_y_x', 'Test_Date', 'CREI_x', 'DATE_DLBCL Diagnosis_x', 'tests months diagnosis_x', 'Unnamed: 0_y', 'ID_x_y', 'CLINIC_ID_x_y', 'DOCTOR_ID_x_y', 'ORDERING_WORKSTATION_ID_x_y', 'Test Date_x',  'Unnamed: 0.1_y', 'ID_y_y', 'CLINIC_ID_y_y', 'DOCTOR_ID_y_y', 'ORDERING_WORKSTATION_ID_y_y', 'Test Date_y', 'Progression post RCHOP (yes = 1, no=0)_y', 'DATE_DLBCL Diagnosis_y', 'tests months diagnosis_y']
,axis=1)

both_relapse.rename(columns={'GLUCOSE_y': 'GLUCOSE'}, inplace=True)
both_no_relapse.rename(columns={'GLUCOSE_y': 'GLUCOSE'}, inplace=True)
both_relapse.rename(columns={'CREI_y': 'CREI'}, inplace=True)
both_no_relapse.rename(columns={'CREI_y': 'CREI'}, inplace=True)
# #
# # #check the right columns are left and there are no NaN values
both_relapse = both_relapse.loc[:,~both_relapse.columns.duplicated()]
both_no_relapse = both_no_relapse.loc[:,~both_no_relapse.columns.duplicated()]


print(list(both_relapse.columns))
print(list(both_no_relapse.columns))



# #
print(both_no_relapse.isnull().sum())
print(both_relapse.isnull().sum())
# #
dataset=pd.concat([both_no_relapse, both_relapse], ignore_index=True, sort=False)
# #
# # print(dataset.shape)
# # print(dataset.head(1))
# # print("#########################")
# #
# # #splitting the dataset into x and y datasets
x_dataset = dataset.iloc[:, 1:22]
y_dataset= dataset.iloc[:, 0:1]
print(x_dataset)
print(y_dataset)
# #
print(x_dataset.isnull().sum())
# #
# # null_columns=x_dataset.columns[x_dataset.isnull().any()]
# # print(x_dataset[x_dataset.isnull().any(axis=1)][null_columns].head())
# #
#saving names of features and classes
feature_names = x_dataset.columns
class_names = y_dataset.columns
# # #
# # #
# # # x_dataset["ALTI"] = pd.to_numeric(x_dataset["ALTI"],errors='coerce')
# # # x_dataset["BILTI"] = pd.to_numeric(x_dataset["BILTI"],errors='coerce')
# # # x_dataset["GGTI"] = pd.to_numeric(x_dataset["GGTI"],errors='coerce')
# # #
# # #
# # #
# #
# # #preparing the data for the ML model
x_dataset =x_dataset.to_numpy()
y_dataset=y_dataset.to_numpy()
print(y_dataset.shape)
y_dataset=y_dataset.flatten()
y_dataset=y_dataset.transpose()
# y_dataset=y_dataset.astype(int)
print(y_dataset.shape)
sc = StandardScaler()
#
# # #creating test, train and val sets
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.4, random_state=42,stratify=y_dataset)


# #normalizing the x datasets
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)








print("------------ X DATASET POINTS ---------")
print("x train:" , X_train.size, " x test: " ,X_test.size," x_train: ", X_train.size)
print("------------ Y DATASET POINTS  --------")
print("y train:" ,  y_train.size, " y test: " ,y_test.size," y_train: ", y_train.size)
print("------------END ---------")
#
#
clf=RandomForestClassifier(n_estimators=100,oob_score=True)

# clf = LinearDiscriminantAnalysis()


# clf.fit(X_train,y_train)
#
# y_val=clf.predict(X_test)
# #


clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(y_test,y_pred))
print("Balanaced Accuracy: ", metrics.balanced_accuracy_score(y_test,y_pred))
print(metrics.classification_report(y_test,y_pred))

pred_y_test = clf.predict(X_test)

print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print("TESTS USING TEST SET")
print(metrics.classification_report(y_test, pred_y_test))
print("Accuracy: ", metrics.accuracy_score(y_test, pred_y_test))
print("Balanaced Accuracy: ", metrics.balanced_accuracy_score(y_test, pred_y_test))



rand = random.randint(0, 456)
print("Index: ", rand," Y: Predicated: ", pred_y_test[rand])

print("Index: ",rand,"Y: Real: ",y_test[rand])


x=0



# for y in range (0,484):
#         if y_test[y]==pred_y_test[y]:
#          x=x+1
#
# print("test set Accuracy:", (x/484))

y_prob = clf.predict_proba(X_test)
print("AUC: ",roc_auc_score(y_test, y_prob[:, 1]))





# probability = clf.predict_proba(X_test)[:,1]
# print(probability)




fpr, tpr, threshold = metrics.roc_curve(y_test, y_prob[:, 1])
roc_auc = metrics.auc(fpr, tpr)

# method I: plt

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.savefig('BILCHEM ALL VALUES ML-MODEL-auc - accuracy.png', dpi=400)
plt.show()

importances = clf.feature_importances_

std = np.std([tree.feature_importances_ for tree in clf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

print("Feature ranking:")

for f in range(X_test.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure(figsize=(25,10))
# plt.figure()
plt.title("Feature importances")
plt.bar(range(X_test.shape[1]), importances[indices],
       color="b", yerr=std[indices], align="center", width=0.8)
plt.xticks(range(X_test.shape[1]), feature_names[indices])
plt.xlim([-1, X_test.shape[1]])
plt.ylabel('Feature Importance')
plt.savefig('BIOCHEM ALL VALUES ML-MODEL-feature_importance - accuracy.png', dpi=400)
plt.show()



cm=confusion_matrix(y_test, pred_y_test)
print(cm)

tn= cm[0,0]
fn= cm[1,0]
tp= cm[1,1]
fp= cm[0,1]

print("True Negatives: ", tn)
print("False Negatives: ", fn)
print("True Positives: ", tp)
print("False Positives: ", fp)

acc_confusion= ((tp+tn)/(tp+tn+fp+fn))


print("Accuracy of confusion matrix: ",acc_confusion)

# scores = cross_val_score(clf, x_dataset, y_dataset, cv=5)
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
















# #############################################
# #############################################
# #############################################
# #############################################
# #load datasets (liver func / crei / glucose)
# both_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/RELAPSE_MERGE_ALL.xlsx')
# both_no_relapse = pd.read_excel('clean_Data/DLBCL_BIOCHEM/NONRELAPSE_MERGE_ALL.xlsx')
#
# both_relapse = both_relapse.loc[(both_relapse['tests weeks prior relapse'] >= 0) & (both_relapse['tests weeks prior relapse'] <= 28)]
# both_no_relapse = both_no_relapse.loc[(both_no_relapse['tests months diagnosis'] >= 24)]
#
#
# #drop columns we dont need in our model
# both_relapse = both_relapse.drop(['Unnamed: 0', 'ID_x', 'ORDER_ID', 'CLINIC_ID_x', 'DOCTOR_ID_x', 'ORDERING_WORKSTATION_ID_x',
#                                   'Test Date_x', 'Unnamed: 0.1', 'ID_y', 'CLINIC_ID_y', 'DOCTOR_ID_y',
#                                   'ORDERING_WORKSTATION_ID_y', 'Test Date_y',
#                                   'DATE_DLBCL Diagnosis', 'tests months diagnosis','tests weeks prior relapse','Date Prog after RCHOP for DLBCL'],axis=1)
# both_no_relapse = both_no_relapse.drop(['Unnamed: 0', 'ID_x', 'ORDER_ID', 'CLINIC_ID_x', 'DOCTOR_ID_x', 'ORDERING_WORKSTATION_ID_x',
#                                   'Test Date_x', 'Unnamed: 0.1', 'ID_y', 'CLINIC_ID_y', 'DOCTOR_ID_y',
#                                   'ORDERING_WORKSTATION_ID_y', 'Test Date_y',
#                                   'DATE_DLBCL Diagnosis', 'tests months diagnosis'],axis=1)
#
# #check the right columns are left and there are no NaN values
# print(list(both_no_relapse.columns))
# print(list(both_relapse.columns))
#
# print(both_no_relapse.isnull().sum())
# print(both_relapse.isnull().sum())
#
# dataset=pd.concat([both_no_relapse, both_relapse], ignore_index=True, sort=False)
#
# print(dataset.shape)
# print(dataset.head(1))
# print("#########################")
#
# #splitting the dataset into x and y datasets
# x_dataset = dataset.iloc[:, 0:5]
# y_dataset = dataset.iloc[:, 5:6]
#
# print(x_dataset.isnull().sum())
#
# null_columns=x_dataset.columns[x_dataset.isnull().any()]
# print(x_dataset[x_dataset.isnull().any(axis=1)][null_columns].head())
#
# #saving names of features and classes
# feature_names = x_dataset.columns
# class_names = y_dataset.columns
#
#
# x_dataset["ALTI"] = pd.to_numeric(x_dataset["ALTI"],errors='coerce')
# x_dataset["BILTI"] = pd.to_numeric(x_dataset["BILTI"],errors='coerce')
# x_dataset["GGTI"] = pd.to_numeric(x_dataset["GGTI"],errors='coerce')
#
#
#
#
# #preparing the data for the ML model
# x_dataset =x_dataset.to_numpy()
# y_dataset=y_dataset.to_numpy()
# print(y_dataset.shape)
# y_dataset=y_dataset.flatten()
# y_dataset=y_dataset.transpose()
# # y_dataset=y_dataset.astype(int)
# print(y_dataset.shape)
# sc = StandardScaler()
#
# #creating test, train and val sets
# X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.3, random_state=42)
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
#
# #normalizing the x datasets
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)
# X_val = sc.transform(X_val)
#
#
#
#
#
#
#
# print("------------ X DATASET POINTS ---------")
# print("x train:" , X_train.size, " x test: " ,X_test.size," x_train: ", X_train.size," x val: ", X_val.size )
# print("------------ Y DATASET POINTS  --------")
# print("y train:" ,  y_train.size, " y test: " ,y_test.size," y_train: ", y_train.size," x val: ", y_val.size )
# print("------------END ---------")
#
#
# clf=RandomForestClassifier(n_estimators=100,oob_score=True)
#
# # clf = LinearDiscriminantAnalysis()
#
#
# # clf.fit(X_train,y_train)
# #
# # y_val=clf.predict(X_test)
# # #
#
#
# clf.fit(X_train,y_train)
#
# y_pred = clf.predict(X_val)
#
# print("Accuracy: ", metrics.accuracy_score(y_val,y_pred))
# print("Balanaced Accuracy: ", metrics.balanced_accuracy_score(y_val,y_pred))
# print(metrics.classification_report(y_val,y_pred))
#
# pred_y_test = clf.predict(X_test)
#
# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")
# print("-------------------------------------------------------------------")
# print("TESTS USING TEST SET")
# print(metrics.classification_report(y_test, pred_y_test))
# print("Accuracy: ", metrics.accuracy_score(y_test, pred_y_test))
# print("Balanaced Accuracy: ", metrics.balanced_accuracy_score(y_test, pred_y_test))
#
#
#
# rand = random.randint(0, 456)
# print("Index: ", rand," Y: Predicated: ", pred_y_test[rand])
#
# print("Index: ",rand,"Y: Real: ",y_test[rand])
#
#
# x=0
#
# # for y in range (0,578):
# #         if y_test[y]==pred_x_test[y]:
# #          x=x+1
#
# for y in range (0,578):
#         if y_test[y]==pred_y_test[y]:
#          x=x+1
#
# print("test set Accuracy:", (x/578))
#
# y_prob = clf.predict_proba(X_test)
# print("AUC: ",roc_auc_score(y_test, y_prob[:, 1]))
#
#
#
#
#
# # probability = clf.predict_proba(X_test)[:,1]
# # print(probability)
#
#
#
#
# fpr, tpr, threshold = metrics.roc_curve(y_test, y_prob[:, 1])
# roc_auc = metrics.auc(fpr, tpr)
#
# # method I: plt
#
# plt.title('Receiver Operating Characteristic')
# plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
# plt.legend(loc = 'lower right')
# plt.plot([0, 1], [0, 1],'r--')
# plt.xlim([0, 1])
# plt.ylim([0, 1])
# plt.ylabel('True Positive Rate')
# plt.xlabel('False Positive Rate')
# plt.savefig('ML-MODEL-auc_biochem_gluc_blood - accuracy.png', dpi=400)
# plt.show()
#
# importances = clf.feature_importances_
#
# std = np.std([tree.feature_importances_ for tree in clf.estimators_],
#              axis=0)
# indices = np.argsort(importances)[::-1]
#
# print("Feature ranking:")
#
# for f in range(X_test.shape[1]):
#     print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
#
# # Plot the feature importances of the forest
# plt.figure(figsize=(25,10))
# # plt.figure()
# plt.title("Feature importances")
# plt.bar(range(X_test.shape[1]), importances[indices],
#        color="b", yerr=std[indices], align="center", width=0.8)
# plt.xticks(range(X_test.shape[1]), feature_names[indices])
# plt.xlim([-1, X_test.shape[1]])
# plt.ylabel('Feature Importance')
# plt.savefig('BIOCHEM_gluc_blood ML-MODEL-feature_importance - accuracy.png', dpi=400)
# plt.show()
#
#
#
# cm=confusion_matrix(y_test, pred_y_test)
# print(cm)
#
# tn= cm[0,0]
# fn= cm[1,0]
# tp= cm[1,1]
# fp= cm[0,1]
#
# print("True Negatives: ", tn)
# print("False Negatives: ", fn)
# print("True Positives: ", tp)
# print("False Positives: ", fp)
#
# acc_confusion= ((tp+tn)/(tp+tn+fp+fn))
#
# print("Accuracy of confusion matrix: ",acc_confusion)


