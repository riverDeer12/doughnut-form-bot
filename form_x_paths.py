# age spans
age1825 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
age2535 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
age3545 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
age4555 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
age55 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
age_span = [age1825, age2535, age3545, age4555, age55]

# genders
male = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
female = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
other_gender = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
identify = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
genders = [male, female, other_gender, identify]

# age spans
entryLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
intermediaryLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
seniorLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
executiveLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
working_statuses = [entryLevel, intermediaryLevel, seniorLevel, executiveLevel]

# company size
smallEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
mediumEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
largeEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
multinationalEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
company_levels = [smallEnterprise, mediumEnterprise, largeEnterprise, multinationalEnterprise]

# industry type
it = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
marketing = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
sales = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
manufacturing = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
entertainment = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'
health = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[6]/label/div/div[1]/div/div[3]/div'
education = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[1]/div/div[3]/div'
hospitality = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[8]/label/div/div[1]/div/div[3]/div'
other_industry = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[9]/label/div/div[1]/div/div[3]/div'
industry_types = [it, marketing, sales, manufacturing, entertainment, health, education, hospitality, other_industry]

# countries
countries = ['Croatia', 'Morocco', 'Slovenia', 'Germany', 'Switzerland']
country_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input'

# ethnicity
ethnicity = ['African', 'Asian', 'Caucasian', 'Hispanic/Latinx', 'Middle Eastern', 'Indigenous/Native American',
             'Pacific Islander', 'Multiracial/Mixed heritage']
ethnicity_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea'

# adaptations
adaptation_yes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]'
adaptation_no = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
adaptation_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea'
adaptations = [adaptation_yes, adaptation_no]

# local_culture_prefs
importance_1 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'
importance_2 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'
importance_3 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'
importance_4 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'
importance_5 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'
local_culture_preferences = [importance_1, importance_2, importance_3, importance_4, importance_5]

# cultural factors
local_culture_factors_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input'
local_culture_factors = ['language', 'social orientation', 'primary values of society', 'living standard',
                         'average salaries', 'geographical location', 'religion']

# specific_product_features
specific_product_features_yes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
specific_product_features_no = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
specific_product_features_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div[2]/textarea'
specific_product_feature_keywords = ['price', 'advertisement', 'marketing', 'packaging', 'design', 'branding']
specific_product_features = [specific_product_features_yes, specific_product_features_no]

# influence
influence_1 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]'
influence_2 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'
influence_3 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'
influence_4 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'
influence_5 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'
influences = [influence_1, influence_2, influence_3, influence_4, influence_5]

# role of language
language_role_1 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'
language_role_2 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'
language_role_3 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'
language_role_4 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'
language_role_5 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'
language_roles = [language_role_1, language_role_2, language_role_3, language_role_4, language_role_5]

# product alignment
product_alignment_1 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'
product_alignment_2 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'
product_alignment_3 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'
product_alignment_4 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'
product_alignment_5 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'
product_alignments = [product_alignment_1, product_alignment_2, product_alignment_3, product_alignment_4,
                      product_alignment_5]

# product cultural adaptation
product_cultural_adaptation_yes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
product_cultural_adaptation_no = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[17]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
product_cultural_adaptation_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div[1]/div[2]/textarea'
product_cultural_adaptations = [product_cultural_adaptation_yes, product_cultural_adaptation_no]

# satisfaction
satisfaction_domestic = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
satisfaction_foreign = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
satisfactions = [satisfaction_foreign, satisfaction_domestic]

# product recommendation
domestic_product_recommendation = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
foreign_product_recommendation = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
product_recommendations = [domestic_product_recommendation, foreign_product_recommendation]

# foreign product pricing
foreign_product_pricing_yes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
foreign_product_pricing_no = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[21]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
foreign_product_pricing = [foreign_product_pricing_yes, foreign_product_pricing_no]

# advertising perception
advertising_perception_1 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'
advertising_perception_2 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'
advertising_perception_3 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'
advertising_perception_4 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'
advertising_perception_5 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'
advertising_perceptions = [advertising_perception_1, advertising_perception_2, advertising_perception_3,
                           advertising_perception_4, advertising_perception_5]

# product design perception
product_design_1 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'
product_design_2 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'
product_design_3 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'
product_design_4 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'
product_design_5 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'
product_designs = [product_design_1, product_design_2, product_design_3, product_design_4, product_design_5]
