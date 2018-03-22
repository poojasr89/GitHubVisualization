import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('..\data_for_public_release\data_for_public_release\survey_data.csv')



Education_data = data[(data.STATUS == 'Complete')][['FORMAL.EDUCATION', 'PARENTS.FORMAL.EDUCATION']]

print(Education_data.head())

print('==========================================')

Education_data.replace({'FORMAL.EDUCATION': 'Less than secondary (high) school', 'PARENTS.FORMAL.EDUCATION': 'Less than secondary (high) school'}, 0, inplace = True)

Education_data.replace({'FORMAL.EDUCATION': 'Secondary (high) school graduate or equivalent', 'PARENTS.FORMAL.EDUCATION': 'Secondary (high) school graduate or equivalent'}, 1, inplace = True)

Education_data.replace({'FORMAL.EDUCATION': 'Some college, no degree', 'PARENTS.FORMAL.EDUCATION': 'Some college, no degree'}, 2, inplace = True)

Education_data.replace({'FORMAL.EDUCATION': 'Vocational/trade program or apprenticeship', 'PARENTS.FORMAL.EDUCATION': 'Vocational/trade program or apprenticeship'}, 3, inplace = True)

Education_data.replace({'FORMAL.EDUCATION': "Bachelor's degree", 'PARENTS.FORMAL.EDUCATION': "Bachelor's degree"}, 4, inplace = True)

Education_data.replace({'FORMAL.EDUCATION': "Master's degree", 'PARENTS.FORMAL.EDUCATION': "Master's degree"}, 5, inplace = True)

Education_data.replace({'FORMAL.EDUCATION': "Doctorate (Ph.D.) or other advanced degree (e.g. M.D., J.D.)", 'PARENTS.FORMAL.EDUCATION': "Doctorate (Ph.D.) or other advanced degree (e.g. M.D., J.D.)"}, 6, inplace = True)


print(Education_data.head())

Education_data_sorted_by_parents_education = Education_data.groupby('PARENTS.FORMAL.EDUCATION')

print('==========================================')

print(Education_data_sorted_by_parents_education.count())



print('==========================================')

s = pd.DataFrame(Education_data)

s.rename(columns={'FORMAL.EDUCATION':'education', 'PARENTS.FORMAL.EDUCATION':'Parents_education'}, inplace = True)

print(s[(s.education > s.Parents_education)].head())

print('==========================================')

fig, axes = plt.subplots()

handle = pd.concat([s[(s.education <= s.Parents_education)].groupby('Parents_education').count(), s[(s.education >= s.Parents_education)].groupby('Parents_education').count()], axis = 1).plot.bar(ax = axes)

axes.set_xticks([0, 1, 2, 3, 4, 5, 6]);axes.set_xticklabels(('Secondary school','High school','College','Vocational','BS','MS','PhD')); axes.tick_params(axis = 'x', labelrotation = 1);

handle.legend(['Less education than parents', 'More education than parents']); handle.set_xlabel('Education of parents', fontsize=15); handle.set_title("Relationship between parents' and childrens' education", fontsize=15); 

handle.set_ylabel('Number of people', fontsize=15)

#means1 = s[(s.education <= s.Parents_education)].groupby('Parents_education').count()


#means2 = s[(s.education >= s.Parents_education)].groupby('Parents_education').count()

#ind = np.arange(len(means1))

#width = .35

#fig, axes = plt.subplots()

#axes.bar(ind - width/2, height = means2, width = width, color = 'purple', label = "More education than parents")

#axes.bar(ind + width/2, height = means1, width = width, color = 'IndianRed', label = 'Less education than parents')

#axes.set_ylabel('Number of People')

#axes.set_xlabel('Parent Education')

#axes.set_xticks(ind)

#axes.set_xticklabels(('Secondary school','High school','College','Vocational','BS','MS','PhD'))

#axes.set_title('Education Distribution')

#axes.legend()

plt.show()