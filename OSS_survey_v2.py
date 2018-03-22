import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('..\data_for_public_release\data_for_public_release\survey_data.csv')

data_completed_survey = data[(data.STATUS == 'Complete')]

s = data_completed_survey['GENDER']

print(s[s == 'Non-binary or other'].count())

fig1, axes1 = plt.subplots()

axes1.pie([s[s == 'Man'].count(), s[s == 'Woman'].count(), s[s == 'Prefer not to say'].count()], explode = (0,.1,0), labels = ['Men', 'Women', 'Shall_Not_Say'])

#data_completed_survey['GENDER'].plot.pie()

axes1.axis('equal')

axes1.set_title('Gender Consensus of Github Survey')

plt.show()