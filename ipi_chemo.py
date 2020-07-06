import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#using BMI calc from https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/healthy-weights/canadian-guidelines-body-weight-classification-adults/body-mass-index-nomogram.html


#Load dataframes from excel file into pandas
# ipi = pd.read_excel('clean_data/IPI_CHEMO/RES_ID_DLBCL June1 2020 for Moneeza and Matt.xlsx')
# chemo_dates = pd.read_excel('clean_data/IPI_CHEMO/RES_ID_DLBCL_IPI_chemodates_updated.xlsx')




# join = pd.merge(ipi,chemo_dates,on='RES_ID')

# writer = pd.ExcelWriter('clean_Data/chemo_date_ipi_join.xlsx', engine='xlsxwriter')
# join.to_excel(writer, sheet_name='Sheet1')
# writer.save()
#
# bmiCalc = pd.read_excel('clean_Data/chemo_date_ipi_join_non_relapse.xlsx')
# dm2 = pd.read_excel('clean_data/IPI_CHEMO/first_occur_dm2_non_relapse_ipi_bmi.xlsx')
#
#
# #iterate over rows of dataframe, see the value of bmi and assign the classification and risk
#
# for index,row in bmiCalc.iterrows():
#     if row.BMI < 18.5 and row.BMI > 0:
#         bmiCalc.at[index, 'Classification'] ="Underweight"
#         bmiCalc.at[index, 'Risk'] = "Increased"
#     elif row.BMI >= 18.5 and row.BMI <= 24.999999:
#         bmiCalc.at[index, 'Classification'] ="Normal Weight"
#         bmiCalc.at[index, 'Risk'] = "Least"
#     elif row.BMI >= 25.0 and row.BMI <= 29.999999:
#         bmiCalc.at[index, 'Classification'] ="Overweight"
#         bmiCalc.at[index, 'Risk'] = "Increased"
#     elif row.BMI >= 30.0 and row.BMI <= 34.999999:
#         bmiCalc.at[index, 'Classification'] ="Obese class I"
#         bmiCalc.at[index, 'Risk'] = "High"
#     elif row.BMI >= 35.0 and row.BMI <= 39.999999:
#         bmiCalc.at[index, 'Classification'] = "Obese class II"
#         bmiCalc.at[index, 'Risk'] = "Very High"
#     elif row.BMI >= 40:
#         bmiCalc.at[index, 'Classification'] = "Obese class III"
#         bmiCalc.at[index, 'Risk'] = "Extremely High"



# writer = pd.ExcelWriter('clean_Data/chemo_date_ipi_join_bmi_calc.xlsx', engine='xlsxwriter')
# bmiCalc.to_excel(writer, sheet_name='Sheet1')
# writer.save()

# bmiCalc = bmiCalc[['RES_ID','IPI_DX','BMI','Classification','Risk']]
# print(bmiCalc.head(1))
# newJoin = pd.merge(bmiCalc,dm2,on='RES_ID')
# #
# writer = pd.ExcelWriter('clean_Data/ipi_first_dm2_bmi.xlsx', engine='xlsxwriter')
# newJoin.to_excel(writer, sheet_name='Sheet1')
# writer.save()

#Load dataframes from excel file into pandas
gluc = pd.read_excel('clean_data/glui_chemh_only.xlsx')
ipi = pd.read_excel('clean_data/ipi_dm2_non_relapse_bmi.xlsx')


# ipi = ipi.drop(columns=['ORDER_ID', 'CLINIC_ID', 'DOCTOR_ID', 'ORDERING_WORKSTATION_ID', 'Test Date', 'GLUCOSE',  'tests months diagnosis', 'test days diagnosis',  'Unnamed: 15', 'Unnamed: 16'])
#
# #merge together
# newJoin = pd.merge(gluc, ipi, on='RES_ID')
#
# print(newJoin.head(10))
#
# newJoin = newJoin.drop_duplicates(subset ='ORDER_ID',
#                      keep = "first")
# print(newJoin.head(10))
#
# chemo_dates = pd.read_excel('clean_data/IPI_CHEMO/RES_ID_DLBCL_IPI_chemodates_updated.xlsx')
#
# chemo_dates = chemo_dates.drop(columns=['disease', 'extranodal', 'location', 'IPI', 'Stage',  'ECOG', 'weight kg (at last chemo)', 'height (cm)', '#cycles completed', 'radiation', 'history of DM2', 'Unnamed: 15'])
# print(list(chemo_dates.columns))
#
# newJoin1 = pd.merge(newJoin, chemo_dates, on='RES_ID')
#
# writer = pd.ExcelWriter('clean_Data/ipi_first_dm2_bmi_chemh_only_chemo_dates.xlsx', engine='xlsxwriter')
# newJoin1.to_excel(writer, sheet_name='Sheet1')
# writer.save()

#add more chemh data to the glucose values
gluc = pd.read_excel('clean_data/glui_chemh_only.xlsx')