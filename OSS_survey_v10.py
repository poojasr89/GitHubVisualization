import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('..\data_for_public_release\data_for_public_release\survey_data.csv')



men = data[(data.STATUS == 'Complete') & (data.GENDER == 'Woman')]['FORMAL.EDUCATION']

parents_of_men = data[(data.STATUS == 'Complete') & (data.GENDER == 'Woman')]['PARENTS.FORMAL.EDUCATION']

means1 = ( men[men == 'Less than secondary (high) school'].count(), men[men == 'Secondary (high) school graduate or equivalent'].count(), men[men == 'Some college, no degree'].count(), men[men == 'Vocational/trade program or apprenticeship'].count(), men[men == "Bachelor's degree"].count(), men[men == "Master's degree"].count(), men[men == "Doctorate (Ph.D.) or other advanced degree (e.g. M.D., J.D.)"].count())

means2 = (parents_of_men[parents_of_men == 'Less than secondary (high) school'].count(), parents_of_men[parents_of_men == 'Secondary (high) school graduate or equivalent'].count(), parents_of_men[parents_of_men == 'Some college, no degree'].count(), parents_of_men[parents_of_men == 'Vocational/trade program or apprenticeship'].count(), parents_of_men[parents_of_men == "Bachelor's degree"].count(), parents_of_men[parents_of_men == "Master's degree"].count(), parents_of_men[parents_of_men == "Doctorate (Ph.D.) or other advanced degree (e.g. M.D., J.D.)"].count())

ind = np.arange(len(means1))

width = .35

fig, axes = plt.subplots()

axes.bar(ind - width/2, height = means2, width = width, color = 'purple', label = "Women Surveyors' Parents")

axes.bar(ind + width/2, height = means1, width = width, color = 'IndianRed', label = 'Women Surveyors')

axes.set_ylabel('Surveyors')

axes.set_xticks(ind)

axes.set_xticklabels(('Secondary school','High school','College','Vocational','BS','MS','PhD'))

axes.set_title('Education Distribution')

axes.legend()

plt.show()