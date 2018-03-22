import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('..\data_for_public_release\data_for_public_release\survey_data.csv')



men = data[(data.STATUS == 'Complete') & (data.GENDER == 'Man')]['FORMAL.EDUCATION']

women = data[(data.STATUS == 'Complete') & (data.GENDER == 'Woman')]['FORMAL.EDUCATION']




fig, axes = plt.subplots(1,2)

axes[0].pie([men[men == 'Less than secondary (high) school'].count(), men[men == 'Secondary (high) school graduate or equivalent'].count(), men[men == 'Some college, no degree'].count(), men[men == 'Vocational/trade program or apprenticeship'].count(), men[men == "Bachelor's degree"].count(), men[men == "Master's degree"].count(), men[men == "Doctorate (Ph.D.) or other advanced degree (e.g. M.D., J.D.)"].count()], labels = ['Less than high school', 'High school', 'college non-degree', 'Vocational', 'Bachelors', 'Masters', 'PhD'])

axes[0].axis('equal'); axes[0].set_title('Education Distribution of Men who completed Github survey')

axes[1].pie([women[women == 'Less than secondary (high) school'].count(), women[women == 'Secondary (high) school graduate or equivalent'].count(), women[women == 'Some college, no degree'].count(), women[women == 'Vocational/trade program or apprenticeship'].count(), women[women == "Bachelor's degree"].count(), women[women == "Master's degree"].count(), women[women == "Doctorate (Ph.D.) or other advanced degree (e.g. M.D., J.D.)"].count()], labels = ['Less than high school', 'High school', 'college non-degree', 'Vocational', 'Bachelors', 'Masters', 'PhD'])


axes[1].axis('equal'); axes[1].set_title('Education Distribution of Women who completed Github survey')

plt.show()