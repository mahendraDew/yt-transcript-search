# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains

# import time
# import os

# from dotenv import load_dotenv

# load_dotenv()


# # meeting_url = input("Enter Webex meeting URL: ")
# meeting_url = os.getenv("WEBEX_MEETING_URL")



# # --- Setup Chrome options ---
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-features=ProtocolHandlers")  # stops xdg-open popup

# driver = webdriver.Chrome(options=options)

# try:
#     # --- Open Webex link ---
#     driver.get(meeting_url)
    

    
    
#     # --- Wait for "Join from your browser" to appear button and click it ---
#     print("now clicking on the join button...")
#     button_element = driver.find_element(By.ID, "broadcom-center-right") 
#     actions = ActionChains(driver)
#     actions.click(button_element).perform()
    
#     print("Clicked 'Join from your browser' successfully!")

#     #TODO: dont sleep instead implement logic to wait till page gets loaded instead just waiting for 10 sec
#     # time.sleep(10)

#     # driver.implicitly_wait(2)


  
#     try: 
     
#         print("Entering name....")

#         # wait until the iframe is present
#         iframe = WebDriverWait(driver, 15).until(
#             EC.presence_of_element_located((By.ID, "unified-webclient-iframe"))
#         )

#         # switch into the iframe
#         driver.switch_to.frame(iframe)

#         # now find your input inside the iframe
#         name_input = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test="Name (required)"]'))
#         )

#         name_input.send_keys("summarizeBOT")

#         # data-test="join-button"
#         time.sleep(4)
#         # join_btn = driver.find_element(By.CSS_SELECTOR, 'input[data-test="join-button"]') # Replace with appropriate locator and value
#         join_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, 'mdc-button[data-test="join-button"]'))
#         )

#         print("join btn", join_button)
#         print("Clicking Join button....")
#         actions.click(join_button).perform()
        


#     except Exception as e:
#         print("err occured:", e)

#     time.sleep(80)
# except Exception as e:
#     print("err:", e)

# finally:
#     pass
#     # driver.quit()  # close browser when done


from webex_spawner import WebexSpawner

if __name__ == "__main__":
    # webex spawner - create a chrome instance and spawn a webex meet 
    spawner = WebexSpawner()
    spawner.run()


    