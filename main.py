# from my_package import say_hi


# say_hi()

# print("hi from main ubu")

########################################################################################


# driver installation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


print("starting main....")

driver = webdriver.Chrome()

# taking the webex meeting url
driver.get('https://meetingsapac33.webex.com/meet/pr1762655274')

# elem = driver.find_element(By.ID, 'm-documentationwebdriver')
# elem.click()
# assert 'WebDriver' in driver.title


time.sleep(10)





# quit the driver
# driver.quit()
