from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import os
from dotenv import load_dotenv
import time

class WebexSpawner:
    def __init__(self):
        load_dotenv()
        self.meeting_url = os.getenv("WEBEX_MEETING_URL")

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-features=ProtocolHandlers")

        self.driver = webdriver.Chrome(options=options)
        self.actions = ActionChains(self.driver)

    def open_meeting(self):
        print("[Task 1] Opening Webex meeting link...")
        self.driver.get(self.meeting_url)

    def click_join_browser(self):
        print("[Task 2] Clicking 'Join from your browser'...")
        join_browser_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "broadcom-center-right"))
        )
        self.actions.click(join_browser_btn).perform()
        print("Clicked 'Join from your browser'")

    def enter_name(self, bot_name="summarizeBOT"):
        print("[Task 3] Entering name...")

        # Switch to iframe
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "unified-webclient-iframe"))
        )
        self.driver.switch_to.frame(iframe)

        # Type into input
        name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test="Name (required)"]'))
        )
        name_input.clear()
        name_input.send_keys(bot_name)
        print(f"Entered name '{bot_name}'")

    def click_join_meeting(self):
        print("[Task 4] Clicking 'Join' button...")
        join_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'mdc-button[data-test="join-button"]'))
        )
        self.actions.click(join_button).perform()
        print("waiting for someone to let me in!")

    def confirm_meeting_entry(self):
        print("[Task 5] Waiting for meeting confirmation...")

        try:
            meeting_banner = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//mdc-text[contains(text(), "You\'re now in the meeting")]')
                )
            )
            if meeting_banner:
                print("You are in the meeting")
        except Exception:
            print("⚠️ Could not confirm meeting entry (banner not found)")

    def run(self):
        try:
            self.open_meeting()
            self.click_join_browser()
            self.enter_name()
            self.click_join_meeting()
            self.confirm_meeting_entry()   

            time.sleep(80)  # Keep session alive for now
        except Exception as e:
            print("Error:", e)
        finally:
            pass
            # self.driver.quit()  # Uncomment if you want to close after done
