import random

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSchR--zcSUXsAtjNGg6vfvW7X896LYvLhzt_4A9M7GtYY0Y-Q/viewform')

# age spans
age1825 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
age2535 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
age3545 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
age4555 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
age55 = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div'

# genders
male = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
female = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
other_gender = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
identify = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

# age spans
entryLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
intermediaryLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
seniorLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
executiveLevel = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

# company size
smallEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
mediumEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
largeEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
multinationalEnterprise = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'

# industry type
it = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div'
marketing = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'
sales = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div'
manufacturing = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div'
entertainment = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[6]/label/div/div[1]/div/div[3]/div'
health = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[7]/label/div/div[1]/div/div[3]/div'
education = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[8]/label/div/div[1]/div/div[3]/div'
hospitality = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[9]/label/div/div[1]/div/div[3]/div'
other_industry = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[10]/label/div/div[1]/div/div[3]/div'

# countries
countries = ['Croatia', 'Morocco', 'Slovenia', 'Germany', 'Switzerland']

# ethnicity
ethnicity = ['African', 'Asian', 'Caucasian', 'Hispanic/Latinx', 'Middle Eastern', 'Indigenous/Native American',
             'Pacific Islander', 'Multiracial/Mixed heritage']

# adaptations
adaptation_yes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]'
adaptation_no = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div'


# local_culture_prefs
importance_1 = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div"
importance_2 = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div"
importance_3 = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div"
importance_4 = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div"
importance_5 = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"

# answer arrays
age_span = [age1825, age2535, age3545, age4555, age55]
genders = [male, female, other_gender, identify]
working_statuses = [entryLevel, intermediaryLevel, seniorLevel, executiveLevel]
company_level = [smallEnterprise, mediumEnterprise, largeEnterprise, multinationalEnterprise]
industry_type = [it, marketing, sales, manufacturing, entertainment, health, education, hospitality, other_industry]
adaptations = [adaptation_yes, adaptation_no]
local_culture_prefs = [importance_1, importance_2, importance_3, importance_4, importance_5]

# click actions
driver.find_element(By.XPATH, random.choice(age_span)).click()
driver.find_element(By.XPATH, random.choice(genders)).click()
driver.find_element(By.XPATH, random.choice(working_statuses)).click()
driver.find_element(By.XPATH, random.choice(company_level)).click()
driver.find_element(By.XPATH, random.choice(industry_type)).click()
driver.find_element(By.XPATH, random.choice(adaptations)).click()
driver.find_element(By.XPATH, random.choice(local_culture_prefs)).click()

