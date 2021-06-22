import pandas as pd
import numpy as np


relapse = pd.read_excel('clean_Data/relapse-non-relapse/Progression_Blood_RES_DAY_CLEAN.xlsx')
relapse = relapse.loc[(relapse['#_of_Years_tests_post'] >= 0) & (relapse['#_of_Years_tests_post'] <= 28)]

nonrelapse = pd.read_excel('clean_Data/relapse-non-relapse/No_Progression_Blood_RES_MONTH_CLEAN.xlsx')
nonrelapse = nonrelapse.loc[(nonrelapse['#_of_Years_tests_post'] >= 36)]
nonrelapse = nonrelapse.drop(['Unnamed: 0','DATE_DLBCL Diagnosis','#_of_Years_tests_post','ORDER'],axis=1)
nonrelapse=nonrelapse.reset_index(drop=True)





relapse_unique = relapse.ID.unique()
nonrelapse_unique = nonrelapse.ID.unique()


print(relapse_unique.size)
print(nonrelapse_unique.size)

# df = pd.DataFrame(data=relapse_unique.flatten())
#
# writer = pd.ExcelWriter('clean_Data/N0N123_TEST.xlsx', engine='xlsxwriter')
# #
# df.to_excel(writer, sheet_name='Sheet1')
#
# writer.save()