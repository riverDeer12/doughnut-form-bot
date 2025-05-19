# age groups 1
age1825 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
age2635 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
age3645 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
age46plus = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
age_groups = [age1825, age2635, age3645, age46plus]

# education 2
highschool = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
bachelor = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
master = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
phd = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
education = [highschool, bachelor, master, phd]

# industry 3
technology = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
healthcare = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
retail = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
creative_media = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
industry = [technology, healthcare, retail, creative_media]

# entrepreneur 4
yes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
no_has_plan = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
no = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
entrepreneur = [yes, no_has_plan, no]

# familiarity 5
very_familiar = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
somewhat_familiar = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
neutral = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
not_very_familiar = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
not_familiar_at_all = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
familiarity = [very_familiar, somewhat_familiar, neutral, not_very_familiar, not_familiar_at_all]

# technologies 6
social_media = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[1]'
e_commerce = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[2]/label/div/div[1]'
ai = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[3]/label/div/div[1]'
cloud = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[4]/label/div/div[1]'
digital_payment = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[5]/label/div/div[1]'
technologies = [social_media, e_commerce, ai, cloud, digital_payment]

# extent 7
greatly_improved = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
somewhat_improved = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
neutral = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
somewhat_limited = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
greatly_limited = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
extent = [greatly_improved, somewhat_improved, neutral, somewhat_limited, greatly_limited]

# biggest_challenges 8
lack_technical_skills = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
high_cost = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
cybersecurity = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
diff_reaching_target_audiences = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
high_competition = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
biggest_challenges = [lack_technical_skills, high_cost, cybersecurity, diff_reaching_target_audiences, high_competition]

# digitalization_lowers 9
one_digitalization_lowers = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div/div[1]/div'
two_digitalization_lowers = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div/div/div/div[1]/div'
three_digitalization_lowers = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div/div/div/div[1]/div'
four_digitalization_lowers = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div/div/div/div[1]/div'
five_digitalization_lowers = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div/div[1]/div'
digitalization_lowers = [one_digitalization_lowers, two_digitalization_lowers, three_digitalization_lowers,
                         four_digitalization_lowers, five_digitalization_lowers]

# digital_tools 10
one_digital_tools = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div'
two_digital_tools = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div'
three_digital_tools = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div'
four_digital_tools = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div'
five_digital_tools = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
digital_tools = [one_digital_tools, two_digital_tools, three_digital_tools, four_digital_tools, five_digital_tools]

# government_policies 12
one_government_policies = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div'
two_government_policies = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div'
three_government_policies = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div'
four_government_policies = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div'
five_government_policies = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
government_policies = [one_government_policies, two_government_policies, three_government_policies,
                       four_government_policies, five_government_policies]

# financial_institutions 13
one_financial_institutions = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div'
two_financial_institutions = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div'
three_financial_institutions = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div'
four_financial_institutions = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div'
five_financial_institutions = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
financial_institutions = [one_financial_institutions, two_financial_institutions, three_financial_institutions,
                          four_financial_institutions, five_financial_institutions]

# online_platforms 14
one_online_platforms = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div'
two_online_platforms = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div'
three_online_platforms = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div'
four_online_platforms = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div'
five_online_platforms = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
online_platforms = [one_online_platforms, two_online_platforms, three_online_platforms, four_online_platforms,
                    five_online_platforms]

# future_impact 15
one_future_impact = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
two_future_impact = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
three_future_impact = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
four_future_impact = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
five_future_impact = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
future_impacts = [one_future_impact, two_future_impact, three_future_impact, four_future_impact,
                  five_future_impact]

# skills 16
one_skills = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
two_skills = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
three_skills = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
four_skills = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
five_skills = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
skills = [one_skills, two_skills, three_skills, four_skills,
          five_skills]
