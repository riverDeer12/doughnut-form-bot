from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(chrome_options)

instagram_profile_url = 'https://www.instagram.com/natgeo/'

# call url
driver.maximize_window()
driver.get(instagram_profile_url)

try:
    # Navigate to the Instagram page
    url = "https://www.instagram.com/natgeo"
    driver.get(url)

    # Allow time for the page to load
    time.sleep(5)

    # Find all img elements with the specified class
    img_elements = driver.find_elements(By.CLASS_NAME, "x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")

    # Extract the 'src' attributes from the img elements
    img_sources = [img.get_attribute("src") for img in img_elements]

    # Print the extracted image URLs
    for src in img_sources:
        print(src)

finally:
    # Close the WebDriver
    driver.quit()






