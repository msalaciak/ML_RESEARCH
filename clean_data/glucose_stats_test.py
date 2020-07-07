import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from scipy.stats import ttest_ind
from statsmodels.stats import weightstats as stests
from lifelines import CoxPHFitter
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt



# #Load dataframes from excel file into pandas
# # gluc= pd.read_excel('glucose_stats_prep.xlsx')
# #
# # #all IDS of patients who have glucose over 7.7
# # IDS = [31692, 38309, 73998, 80182, 120281, 132169, 134159, 138663, 152609, 169163, 174503, 177039, 202862, 209211, 224504,
# #        225344, 248356, 278467, 293070, 357200, 358598, 366744, 383572, 410704, 476176, 506702, 510815, 519302, 529134,
# #        550102, 551241, 631717, 649128, 649881, 709607, 711866, 818008, 848066, 916969, 923521, 951190, 951650, 963948,
# #        970198, 972548, 973749, 976141, 1014270, 1022485, 1071857, 1073446, 1072382, 1086241, 1088452, 1086461, 1089394,
# #        1108538, 1112846, 1110718, 1111687, 1111911, 1114608, 1131588, 1128826, 1129603, 1137356, 1151809, 1152165,
# #        1156765, 1186741, 1202062, 1213896, 1218461, 1246774, 1247563, 1267589, 1271382, 1298079, 1313367, 1321225,
# #        1337240, 1345658, 1350999, 1359008, 1394869, 1431309, 1507198, 1519413]
# #
# #
# #
# #
# #
# # #iterate over rows of dataframe, see the value of glucose over 7.7 and assign the value 1 if it is 0
# # for id in IDS:
# #
# #     for index,row in gluc.iterrows():
# #         if row.Over_7_7 == 0 and id==row.RES_ID:
# #             gluc.at[index, 'Over_7_7'] = 1
# #
# #
# # #save
# # writer = pd.ExcelWriter('gluc_stats_filled.xlsx', engine='xlsxwriter')
# # gluc.to_excel(writer, sheet_name='Sheet1')
# # writer.save()

# #Load dataframes from excel file into pandas
dm2= pd.read_excel('gluc_stats_7_group_clean.xlsx')
nodm2 = pd.read_excel('gluc_stats_0_group_clean.xlsx')

#drop duplicates only unique values

dm2.drop_duplicates(subset ="RES_ID",
                     keep = 'first', inplace = True)
nodm2.drop_duplicates(subset ="RES_ID",
                     keep = 'first', inplace = True)

#Print size of datasets
print("over 7.7 ",dm2.shape)
print("under 7.7 " , nodm2.shape,"\n")

#print mean and std of bmi groups
print("over 7.7 mean bmi: ", dm2["BMI"].mean())
print("under 7.7 mean bmi: ", nodm2["BMI"].mean())
print("over 7.7 std bmi: ", dm2["BMI"].std())
print("under 7.7 std bmi: ", nodm2["BMI"].std(),"\n")

#print mean and std of ipi_dx groups
print("over 7.7 mean ipi: ", dm2["IPI_DX"].mean())
print("under 7.7 mean ipi: ", nodm2["IPI_DX"].mean())
print("over 7.7 std ipi: ", dm2["IPI_DX"].std())
print("under 7.7 std ipi: ", nodm2["IPI_DX"].std(),"\n")

#print mean and std of classification cat
print("over 7.7 mean Classification: ", dm2["class_cat"].mean())
print("under 7.7 mean Classification: ", nodm2["class_cat"].mean())
print("over 7.7 std Classification: ", dm2["class_cat"].std())
print("under 7.7 std Classification: ", nodm2["class_cat"].std(),"\n")

#print mean and std of risk cat
print("over 7.7 mean Risk Cat: ", dm2["Risk_Cat"].mean())
print("under 7.7 mean Risk Cat: ", nodm2["Risk_Cat"].mean())
print("over 7.7 std Risk Cat: ", dm2["Risk_Cat"].std())
print("under 7.7 std Risk Cat: ", nodm2["Risk_Cat"].std(),"\n")


#print mean and std of risk order
print("over 7.7 mean Risk Ord: ", dm2["Risk_ord"].mean())
print("under 7.7 mean Risk Ord: ", nodm2["Risk_ord"].mean())
print("over 7.7 std Risk Ord: ", dm2["Risk_ord"].std())
print("under 7.7 std Risk Ord: ", nodm2["Risk_ord"].std(),"\n")

print("BMI:")

ztest ,pval = stests.ztest(x1=dm2['BMI'], x2=nodm2['BMI'], value=0,alternative='two-sided')
print("p-value z-test ",float(pval))
if pval<0.05:
    print("reject null hypothesis \n")
else:
    print("accept null hypothesis \n")



ttest,pval = ttest_ind(dm2['BMI'],nodm2['BMI'])
print("p-value t test",pval)
if pval <0.05:
  print("we reject null hypothesis\n")
else:
  print("we accept null hypothesis\n")

print("IPI_DX:")

ztest ,pval = stests.ztest(x1=dm2['IPI_DX'], x2=nodm2['IPI_DX'], value=0,alternative='two-sided')
print("p-value z-test ",float(pval))
if pval<0.05:
    print("reject null hypothesis \n")
else:
    print("accept null hypothesis \n")



ttest,pval = ttest_ind(dm2['IPI_DX'],nodm2['IPI_DX'])
print("p-value t test",pval)
if pval <0.05:
  print("we reject null hypothesis\n")
else:
  print("we accept null hypothesis\n")



print("RISK_CAT:")


ztest ,pval = stests.ztest(x1=dm2['Risk_Cat'], x2=nodm2['Risk_Cat'], value=0,alternative='two-sided')
print("p-value z-test ",float(pval))
if pval<0.05:
    print("reject null hypothesis \n")
else:
    print("accept null hypothesis \n")



ttest,pval = ttest_ind(dm2['Risk_Cat'],nodm2['Risk_Cat'])
print("p-value t test",pval)
if pval <0.05:
  print("we reject null hypothesis\n")
else:
  print("we accept null hypothesis\n")

print("RISK_ORD:")

ztest ,pval = stests.ztest(x1=dm2['Risk_ord'], x2=nodm2['Risk_ord'], value=0,alternative='two-sided')
print("p-value z-test ",float(pval))
if pval<0.05:
    print("reject null hypothesis \n")
else:
    print("accept null hypothesis \n")



ttest,pval = ttest_ind(dm2['Risk_ord'],nodm2['Risk_ord'])
print("p-value t test",pval)
if pval <0.05:
  print("we reject null hypothesis\n")
else:
  print("we accept null hypothesis\n")

print("CLASS_CAT:")

ztest ,pval = stests.ztest(x1=dm2['class_cat'], x2=nodm2['class_cat'], value=0,alternative='two-sided')
print("p-value z-test ",float(pval))
if pval<0.05:
    print("reject null hypothesis \n")
else:
    print("accept null hypothesis \n")



ttest,pval = ttest_ind(dm2['class_cat'],nodm2['class_cat'])
print("p-value t test",pval)
if pval <0.05:
  print("we reject null hypothesis\n")
else:
  print("we accept null hypothesis\n")



#loading dataset ready for cox hazard
coxdata = pd.read_excel('chemh_full_tests_clean_cox_test_clean.xlsx')



print(coxdata.head(2))

# coxdata.drop('BMI', axis=1, inplace=True)
# coxdata.drop('GLUI', axis=1, inplace=True)

print(coxdata.head(2))

cph = CoxPHFitter()
cph.fit(coxdata, duration_col='event_in_weeks', event_col='Over_7_7',show_progress=True,step_size=0.2)

cph.print_summary()  # access the results using cph.summary
cph.plot()
plt.show()



