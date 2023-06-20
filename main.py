import random
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import form_x_paths as x_paths
import helper_functions as helpers

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

for _ in range(3):

    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSchR--zcSUXsAtjNGg6vfvW7X896LYvLhzt_4A9M7GtYY0Y-Q/viewform'

    # call url
    driver.maximize_window()
    driver.get(form_url)

    # general data
    driver.find_element(By.XPATH, random.choice(x_paths.age_span)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.genders)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.working_statuses)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.company_levels)).click()
    driver.find_element(By.XPATH, x_paths.country_input).send_keys(helpers.select_country())
    driver.find_element(By.XPATH, x_paths.ethnicity_input).send_keys(helpers.select_ethnicity())

    # industry types
    selected_industry_type = random.choice(x_paths.industry_types)
    driver.find_element(By.XPATH, selected_industry_type).click()

    # adaptation
    selected_adaptation = helpers.select_adaptation()

    driver.find_element(By.XPATH, selected_adaptation).click()

    if selected_adaptation == x_paths.adaptation_no:
        driver.find_element(By.XPATH, x_paths.adaptation_input).send_keys('-')
    else:
        driver.find_element(By.XPATH, x_paths.adaptation_input).send_keys(
            helpers.get_adaptation_example(selected_industry_type))

    # local culture and preferences
    driver.find_element(By.XPATH, helpers.select_cultural_prefs_level()).click()
    driver.find_element(By.XPATH, x_paths.local_culture_factors_input).send_keys(
        helpers.generate_input_keywords(x_paths.local_culture_factors))

    # specific features
    driver.find_element(By.XPATH, helpers.select_specific_product_features()).click()
    driver.find_element(By.XPATH, x_paths.specific_product_features_input).send_keys(
        helpers.generate_input_keywords(x_paths.specific_product_feature_keywords))

    # influence
    driver.find_element(By.XPATH, helpers.select_influence_level()).click()

    # role of language
    driver.find_element(By.XPATH, random.choice(x_paths.language_roles)).click()

    # product alignment
    driver.find_element(By.XPATH, random.choice(x_paths.product_alignments)).click()

    # product cultural adaptation
    selected_cultural_adaptation = helpers.select_product_adaptation()

    driver.find_element(By.XPATH, selected_cultural_adaptation).click()

    if selected_cultural_adaptation == x_paths.product_cultural_adaptation_yes:
        driver.find_element(By.XPATH, x_paths.product_cultural_adaptation_input).send_keys(
            helpers.generate_input_keywords(x_paths.specific_product_feature_keywords))
    else:
        driver.find_element(By.XPATH, x_paths.adaptation_input).send_keys('-')

    # satisfaction
    driver.find_element(By.XPATH, random.choice(x_paths.satisfactions)).click()

    # product recommendation
    driver.find_element(By.XPATH, random.choice(x_paths.product_recommendations)).click()

    # foreign product pricing
    driver.find_element(By.XPATH, random.choice(x_paths.foreign_product_pricing)).click()

    # advertising perception
    driver.find_element(By.XPATH, helpers.select_advertising_level()).click()

    # product design perception
    driver.find_element(By.XPATH, helpers.select_design_perception()).click()

    # submit form
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()

    time.sleep(5)
