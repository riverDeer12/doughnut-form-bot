import random
import time
from selenium.webdriver.common.by import By
import form_x_paths as x_paths
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

for _ in range(50):

    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfgb3VYu7ylxlsiMWeBlEThCayukyKcs1r0_aTYybT9jcjFEQ/viewform'

    # call url
    driver.maximize_window()
    driver.get(form_url)

    # general data
    driver.find_element(By.XPATH, random.choice(x_paths.age_span)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.genders)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.current_living)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.environmental_impacts)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.effective_packagings)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.carbon_reducements)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.regulatory_compliances)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.depletions)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.technological_advancements)).click()
    driver.find_element(By.XPATH, random.choice(x_paths.infrastructure_limitations)).click()

    # submit form
    driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span").click()

    time.sleep(5)
