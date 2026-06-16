import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import helper_functions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

for _ in range(54):
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSf4h2-AOAbAV_2ngndfyznEwuw7GOXwQA2sHJJXv_h2MX8TQA/viewform'

    # call url
    driver.maximize_window()
    driver.get(form_url)

    time.sleep(2)

    # general data
    driver.find_element(By.XPATH, helper_functions.select_gender()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_age()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_education()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_shopping_frequency()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_digital_channels()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_digital_commercial_messages()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_digital_content_types()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_brand_ecology()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_ecology()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_brand_company()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_green_marketing()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_brand_campaign()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_higher_price()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_csr_messages()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_recommendations()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_avoid()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_positive_feedback()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_ecological_values()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_company_ecology()).click()

    time.sleep(2)

    # Find and fill the textarea
    textarea = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea')
    textarea.send_keys(helper_functions.select_response())

    time.sleep(2)

    # submit form
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

    time.sleep(10)
