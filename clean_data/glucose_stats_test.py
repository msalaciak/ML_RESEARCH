import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from scipy.stats import ttest_ind
from statsmodels.stats import weightstats as stests


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

print("over 7.7 ",dm2.shape)
print("under 7.7 " , nodm2.shape)

print("over 7.7 mean bmi: ", dm2["BMI"].mean())
print("under 7.7 mean bmi: ", nodm2["BMI"].mean())

print("over 7.7 std bmi: ", dm2["BMI"].std())
print("under 7.7 std bmi: ", nodm2["BMI"].std())





print("over 7.7 mean ipi: ", dm2["IPI_DX"].mean())
print("under 7.7 mean ipi: ", nodm2["IPI_DX"].mean())

print("over 7.7 std ipi: ", dm2["IPI_DX"].std())
print("under 7.7 std ipi: ", nodm2["IPI_DX"].std())

ztest ,pval = stests.ztest(x1=dm2['IPI_DX'], x2=nodm2['IPI_DX'], value=0,alternative='two-sided')
print("p-value z-test ",float(pval))
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")



ttest,pval1 = ttest_ind(dm2['IPI_DX'],nodm2['IPI_DX'])
print("p-value t test",pval1)
if pval1 <0.05:
  print("we reject null hypothesis")
else:
  print("we accept null hypothesis")