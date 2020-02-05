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
import seaborn as sns
from sklearn.tree import export_graphviz
import random

relapse = pd.read_excel('clean_Data/relapse-non-relapse/Progression_Blood_RES_DAY_CLEAN_AGE.xlsx')
nonrelapse = pd.read_excel('clean_Data/relapse-non-relapse/NO_Progression_Blood_RES_DAY_CLEAN_AGE.xlsx')

relapse = relapse.loc[(relapse['#_of_Years_tests_post'] >= 0) & (relapse['#_of_Years_tests_post'] <= 28)]
nonrelapse = nonrelapse.loc[(nonrelapse['#_of_Years_tests_post'] >= 24)]

print(list(relapse.columns))
print(list(nonrelapse.columns))

relapse = relapse.drop(['AGE_TEST','Date of Birth','ID','Unnamed: 0','Date Prog after RCHOP for DLBCL','#_of_Years_tests_post','Test_Date','ORDER','DATE_DLBCL Diagnosis'],axis=1)
nonrelapse = nonrelapse.drop(['AGE_TEST','Date of Birth','ID','Unnamed: 0','#_of_Years_tests_post','Test_Date','ORDER','DATE_DLBCL Diagnosis'],axis=1)
print(list(relapse.columns))
print(list(nonrelapse.columns))


dataset=pd.concat([nonrelapse, relapse], ignore_index=True, sort=False)



x_dataset=dataset.iloc[:, 1:18]

y_dataset= dataset.iloc[:, 0:1]

feature_names = x_dataset.columns



x_dataset =x_dataset.to_numpy()
print(x_dataset.shape)


class_names = y_dataset.columns
y_dataset=y_dataset.to_numpy()
print(y_dataset.shape)
y_dataset=y_dataset.flatten()
y_dataset=y_dataset.transpose()
# y_dataset=y_dataset.astype(int)
print(y_dataset.shape)
sc = StandardScaler()

# x_dataset = StandardScaler().fit_transform(x_dataset)
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.4, random_state=42,stratify=y_dataset)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.3, random_state=42,stratify=y_train)

X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)

X_val = sc.transform(X_val)

# y_train = y_train.transpose()
# y_train = y_train.to_numpy()
# y_train=y_train.astype(int)

# y_test = y_test.transpose()
# y_test = y_test.to_numpy()
# y_test=y_test.astype(int)

# y_val = y_val.transpose()
# y_val = y_val.to_numpy()
# y_val=y_val.astype(int)

# X_train= X_train.reshape(-1, 1)
# X_test = X_test.reshape(-1, 1)
# X_val = X_val.reshape(-1, 1)
#
# y_train= y_train.reshape(-1, 1)
# y_test= y_test.reshape(-1, 1)
# y_val= y_val.reshape(-1, 1)

print("------------ X DATASET POINTS ---------")
print("x train:" , X_train.size, " x test: " ,X_test.size," x_train: ", X_train.size," x val: ", X_val.size )
print("------------ Y DATASET POINTS  --------")
print("y train:" ,  y_train.size, " y test: " ,y_test.size," y_train: ", y_train.size," x val: ", y_val.size )
print("------------END ---------")


clf=RandomForestClassifier(n_estimators=1000,oob_score=True)

# clf = LinearDiscriminantAnalysis()


# clf.fit(X_train,y_train)
#
# y_val=clf.predict(X_test)
# #


clf.fit(X_train,y_train)

y_pred = clf.predict(X_val)

print("Accuracy: ", metrics.accuracy_score(y_val,y_pred))
print("Balanaced Accuracy: ", metrics.balanced_accuracy_score(y_val,y_pred))
print(metrics.classification_report(y_val,y_pred))

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

# for y in range (0,578):
#         if y_test[y]==pred_x_test[y]:
#          x=x+1

for y in range (0,578):
        if y_test[y]==pred_y_test[y]:
         x=x+1

print("test set Accuracy:", (x/578))

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
plt.savefig('ML-MODEL-auc - AGE - accuracy.png', dpi=400)
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
plt.savefig('ML-MODEL-feature_importance - AGE - accuracy.png', dpi=400)
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

