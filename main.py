import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import helper_functions

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

for _ in range(90):
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdWe0eBe4h00hIpf_irPU6pO22Zu3D1pqpghOvhiNhVw1CJjQ/viewform'

    # call url
    driver.maximize_window()
    driver.get(form_url)

    time.sleep(2)

    # general data
    driver.find_element(By.XPATH, helper_functions.select_age()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_education()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_industry()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_entrepreneur()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_familiarity()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_technologies()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_extent()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_biggest_challenges()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_digital_lowers()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_digital_tools()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_government_policies()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_financial_institutions()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_online_platforms()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_future_impact()).click()

    time.sleep(2)

    driver.find_element(By.XPATH, helper_functions.select_skills()).click()

    time.sleep(2)

    # submit form
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span").click()

    time.sleep(10)
