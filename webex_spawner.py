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
        options.add_argument("--use-fake-ui-for-media-stream")
        # options.add_argument("--window-size=1080,720")
        # # options.add_argument("--use-fake-device-for-media-stream")


        '''
             options.addArguments("--disable-blink-features=AutomationControlled");
            options.addArguments("--use-fake-ui-for-media-stream");
            options.addArguments('--auto-select-desktop-capture-source=[RECORD]');
            options.addArguments('--auto-select-desktop-capture-source=[RECORD]');
            options.addArguments('--enable-usermedia-screen-capturing');
            options.addArguments('--auto-select-tab-capture-source-by-title="Meet"')
            options.addArguments('--allow-running-insecure-content');
        
        '''

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
            meeting_banner = WebDriverWait(self.driver, 60*5).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//mdc-text[contains(text(), "You\'re now in the meeting")]')
                )
            )
            if meeting_banner:
                print("You are in the meeting")
        except Exception:
            print("⚠️ Could not confirm meeting entry (banner not found)")

    def start_tab_recording(self, duration_ms=60000):
        print("[Task 6] Staring the screen recording...")

        js_script = """
           function wait(delayInMS) {
            return new Promise((resolve) => setTimeout(resolve, delayInMS));
        }

        function startRecording(stream, lengthInMS) {
            let recorder = new MediaRecorder(stream);
            let data = [];
            
            recorder.ondataavailable = (event) => data.push(event.data);
            recorder.start();
            
            let stopped = new Promise((resolve, reject) => {
                recorder.onstop = resolve;
                recorder.onerror = (event) => reject(event.name);
            });
            
            let recorded = wait(lengthInMS).then(() => {
                if (recorder.state === "recording") {
                recorder.stop();
                }
            });
            
            return Promise.all([stopped, recorded]).then(() => data);
        }
      
        console.log("before mediadevices")
        window.navigator.mediaDevices.getDisplayMedia({
            video: {
              displaySurface: "browser"
            },
            audio: true,
            preferCurrentTab: true
        }).then(async screenStream => {                        
            const audioContext = new AudioContext();
            const screenAudioStream = audioContext.createMediaStreamSource(screenStream)
            const audioEl1 = document.querySelectorAll("audio")[0];
            const audioEl2 = document.querySelectorAll("audio")[1];
            const audioEl3 = document.querySelectorAll("audio")[2];
            const audioElStream1 = audioContext.createMediaStreamSource(audioEl1.srcObject)
            const audioElStream2 = audioContext.createMediaStreamSource(audioEl3.srcObject)
            const audioElStream3 = audioContext.createMediaStreamSource(audioEl2.srcObject)

            const dest = audioContext.createMediaStreamDestination();

            screenAudioStream.connect(dest)
            audioElStream1.connect(dest)
            audioElStream2.connect(dest)
            audioElStream3.connect(dest)

            // window.setInterval(() => {
            //   document.querySelectorAll("audio").forEach(audioEl => {
            //     if (!audioEl.getAttribute("added")) {
            //       console.log("adding new audio");
            //       const audioEl = document.querySelector("audio");
            //       const audioElStream = audioContext.createMediaStreamSource(audioEl.srcObject)
            //       audioEl.setAttribute("added", true);
            //       audioElStream.connect(dest)
            //     }
            //   })

            // }, 2500);
          
          // Combine screen and audio streams
          const combinedStream = new MediaStream([
              ...screenStream.getVideoTracks(),
              ...dest.stream.getAudioTracks()
          ]);
          
          console.log("before start recording")
          const recordedChunks = await startRecording(combinedStream, 60000);
          console.log("after start recording")
          
          let recordedBlob = new Blob(recordedChunks, { type: "video/webm" });
          
          // Create download for video with audio
          const recording = document.createElement("video");
          recording.src = URL.createObjectURL(recordedBlob);
          
          const downloadButton = document.createElement("a");
          downloadButton.href = recording.src;
          downloadButton.download = "RecordedScreenWithAudio.webm";    
          downloadButton.click();
          
          console.log("after download button click")
          
          // Clean up streams
          screenStream.getTracks().forEach(track => track.stop());
          audioStream.getTracks().forEach(track => track.stop());

        })

        """
        try:
            # Execute it in the browser
            self.driver.execute_script(js_script)
            print("recording done")
        except:
            print("some error occured while recording....")
        
        # keep Selenium alive while recording finishes
        self.driver.implicitly_wait(duration_ms/1000 + 5)


    def run(self):
        try:
            self.open_meeting()
            self.click_join_browser()
            self.enter_name()
            self.click_join_meeting()
            self.confirm_meeting_entry()   
            self.start_tab_recording()
            print('keeping the session alive for 100 sec')
            time.sleep(100)  # Keep session alive for now
        except Exception as e:
            print("Error:", e)
        finally:
            pass
            # self.driver.quit()  # Uncomment if you want to close after done
