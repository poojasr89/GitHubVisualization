# GitHubVisualization
Visualization of GitHub survey data
Women have more educative parents than men.

Let us start with a gender consensus of the surveyors who completed the GitHub survey.
gender_consensus: 

OSS_survey_v2.py

Disclaimer: The following analysis may not be a fair comparison since the number of women in the GitHub survey data forms only a very small fraction of the number of men. Nevertheless, we proceed to estimate the influence of education in determining the participation of involvement of women in open source forums. Plot below shows the comparison of education of men and women who participated in the survey.

men_vs_women_education : OSS_survey_v5.py

It can be deduced from the above plot that there is more percentage of men who have education levels of high school and college (non-degree) compared to women. On the other hand, more percentage of women tend to obtain a Bachelor's degree compared to men. The percentage numbers are very similar for men and women who have Master's and PhD degrees. To gain more insight, let us compare the education of parents of men and women surveyors:

parents_of_men_vs_women_education: OSS_survey_v6.py

There seems to be a drastic difference in education of women's parents compared to that of men's. A higher percentage of mens' parents have high school and Bachelor's degrees whereas womens' parents have a higher percentage of Master's and PhD degree holders.

Since we are discussing education among the surveyors and their parents, I thought it be enlightening to do an overall comparison of their education levels:

education_then_and_now: OSS_survey_v9.py

We see that there are more people who have college (both degree and non-degree) education compared to their parents, although the PhD category speaks otherwise! Since the data is dominated by men, the previous comparison could be dominated by statistics of male surveyors and their parents. Let now only focus on female surveyors and compare their education distribution with their parents' education.

education_then_and_now_women: OSS_survey_v10.py 


The pattern follows the general trend shown in the previous bar graph but there is a greater decline in women pursuing Master's and PhD degrees compared to their parents.





Tools used: Python Pandas and matplotlib
