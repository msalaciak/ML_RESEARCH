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

# #all data
lymfit_all = pd.read_excel('FitBitCleaned.xlsx')
# print(lymfit_all.head(10))
#
# #matts data
# lymfit002 = lymfit_all.loc[(lymfit_all['SubjectIdentifier'] == 'LF-01-SC-002')]
# print(lymfit002.head(10))

# #weekly data
lymfit_weekly = pd.read_excel('fitbitweekly.xlsx')
print(lymfit_weekly.head(10))


#BAR GRAPH
# sns.set(style="whitegrid")
#
#
# f, ax = plt.subplots(figsize=(6, 15))
#
# # Load the example car crash dataset
#
#
#
# # Plot the total crashes
# sns.set_color_codes("pastel")
# sns.barplot(x="GoalSteps", y="ActivityDate", data=lymfit002,
#             label="Daily Steps Goal", color="b")
#
# # Plot the crashes where alcohol was involved
# sns.set_color_codes("muted")
# sns.barplot(x="Steps", y="ActivityDate", data=lymfit002,
#             label="Steps per day", color="b")
#
# # Add a legend and informative axis label
# ax.legend(ncol=2, loc="best", frameon=True)
# ax.set(xlim=(0, 20000), ylabel="",
#        xlabel="Daily Steps Goal vs Daily Steps")
# sns.despine(left=True, bottom=True)
#
#
# plt.savefig('lymfit_002_steps_goals', dpi=400)
# plt.show()


# HEAT MAP
# sns.set()
#
# lymfit_weekly = lymfit_weekly.pivot("ActivityDate", "SubjectIdentifier" ,"Steps")
#
# # Draw a heatmap with the numeric values in each cell
# f, ax = plt.subplots(figsize=(10, 5))
# sns.heatmap(lymfit_weekly, annot=True, fmt="d", linewidths=.5, ax=ax ,cmap="PuBu")
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)
#
# ax.set_title('Steps Per Day')
# plt.savefig('steps_goals_heat_map', dpi=400)
#
# plt.show()


# df = lymfit_all.drop(lymfit_weekly.columns[[1, 2, 3,4,6,8,9,10,11,13,16]], axis=1)
# print(df.head(1))
#
# sns.set(style="ticks")
# sns.despine()
#
#
#
#
# g =sns.pairplot(df,hue="SubjectIdentifier")
#
#
#
#
#
#
# g.savefig('data_sum', dpi=400)
#
# plt.show()


#
# sns.set(style="white")
#
# # Load the example mpg dataset
# df = lymfit_all
#
# # Plot miles per gallon against horsepower with other semantics
# g = sns.relplot(x="ActivityCalories", y="VeryActiveMinutes", hue="SubjectIdentifier", size="Steps",
#             sizes=(20, 200), alpha=.5, palette="muted",
#             height=5.5, data=df)
#
# g.savefig('active', dpi=400)
# plt.show()





lymfit_mean = pd.read_excel('FitBitAverage.xlsx')

sns.set(style="white", context="talk")


# Set up the matplotlib figure
f, (ax1, ax2, ax3,ax4,ax5) = plt.subplots(5, 1, figsize=(7, 20), sharex=True)

# Generate some sequential data

splot =sns.barplot(x="Subject Identifier", y="Mean Fairly Active Minutes ", palette="muted", ax=ax1,data=lymfit_mean)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Mean Fairly Active Minutes ")
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')



splot = sns.barplot(x="Subject Identifier", y="Mean Lightly Active Minutes", palette="muted", ax=ax2,data=lymfit_mean)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Mean Lightly Active Minutes")
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')


splot =sns.barplot(x="Subject Identifier", y="Mean Very Active Minutes", palette="muted", ax=ax3,data=lymfit_mean)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("Mean Very Active Minutes")
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

splot =sns.barplot(x="Subject Identifier", y="Mean Steps", palette="muted", ax=ax4,data=lymfit_mean)
ax4.axhline(0, color="k", clip_on=False)
ax4.set_ylabel("Mean Steps")
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

splot = sns.barplot(x="Subject Identifier", y="Mean Resting Heart Rate", palette="muted", ax=ax5,data=lymfit_mean)
ax5.axhline(0, color="k", clip_on=False)
ax5.set_ylabel("Mean Resting Heart Rate")
for p in splot.patches:
    splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

# Finalize the plot

sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)
plt.savefig('mean', dpi=400)
plt.show()


