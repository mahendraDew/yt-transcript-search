import asyncio
from yt_vid_downloader import YoutubeDownloader;
from speech_recognizer import SpeechRecognition;
import subprocess
from ask_meet import SemanticSearching;
def main(): 
    # task 1: download yt video
    print("TASK 1: Downloading youtube video...")
    yt_downloader = YoutubeDownloader()
    yt_link_input = input("Enter yt link: ")
    # yt_link = "https://www.youtube.com/watch?v=8of5w7RgcTc";
    yt_link_nn = "https://www.youtube.com/watch?v=9GJ6XeB-vMg"
    yt_link_py_1min = "https://www.youtube.com/watch?v=vE7Cy5csYbQ"
    
    title = yt_downloader.download_video(yt_link_input, "downloads")
    print(f"DONE: downloaded yt video: {title}")
    # print (title)


    # task 2: yt video extract the transcript from downloaded vid
    print("TASK 2: Transcribing the downloaded video...")
    video_path = f"downloads/{title}.mp4"
    # video_path = f"downloads/Python in 2 Minutes!.mp4"
    print("TASK 2.1: extracting audio...")
    sr = SpeechRecognition()

    audio_path = sr.extract_audio(video_path)
    print("DONE 2.1: extracted the audio...")
    # transcript = sr.transcribe_audio(audio_path)
    print("TASK 2.2: extracting text from audio...")
    transcript_ts = sr.transcribe_with_timestamps(audio_path)  # 30s per chunk
    print("DONE 2.2: extracted the text...")
    print("-----------------------------------")
    # print("Transcript:\n", transcript_ts)


    if transcript_ts:
        # video_title = get_video_title(video_id)
        # file_name = f"{video_id}_{video_title}.txt"
        # file_name = re.sub(r'[\\/*?:"<>|]', '', file_name)  # Remove invalid characters
        # print("transcript found: " , fetched_transcript)
        print('transcript found.')
        # print(transcript_text)
        controller(transcript_ts, video_path)
        

    else:
            print("Unable to download transcript.")
    # else:
    #     print("Invalid YouTube URL.")


def open_video_at_timestamp(video_path, seconds):
    """Open video in VLC at a specific timestamp"""
    try:
        subprocess.run(["vlc", f"--start-time={seconds}", video_path])
    except FileNotFoundError:
        print("VLC not found! Please install VLC or add it to PATH.")


def controller(transcript, vid_path):
    while True:
        print("1. search for a specific phrase and get timestamp?")
        print("2. semantic search")
        print("3. to exit.")
        option = int(input("Enter 1, 2 or 3:"))
        if option == 1:
            sr = SpeechRecognition()

            search_topic = input("Enter a keyword to search: ")
            # try:
            #     for res in results:
            #         print(f"[{res['timestamp']}] {res['text']}")
            #         print(f"Link: {res['yt_link']}\n")
            #     print("Task 2: timestamp(s):")
            print("")
            print('Task 3 : searching for query: ', search_topic)
            results = sr.search_transcript(transcript, search_topic)
            # print("results: ", results)
            # for text, ts,  in results:
            #     print(f"Found at {ts} -> Snippet: {text} \n")


            for match in results:
                # print(match)
                if "error" in match:
                    print(match["error"])
                else:
                    # print("\n")
                    print(f"Found at {match['timestamp']} -> {match['snippet']}")
                    print("\n")
                    choice = input(f"Open video at {match['timestamp']}? (y/n): ")
                    if choice.lower() == "y":
                        open_video_at_timestamp(vid_path, match["seconds"])
        
        elif option == 2:
            print("")
            print('Task 4 : semantic search')
            search_query = input("Enter a query to search: ")

            #perform a semantic search
            sem_searching = SemanticSearching()
            asyncio.run(sem_searching.semanticSearch(transcript, search_query))

        else:
            break

if __name__ == "__main__":
    main()
    # sem_searching = SemanticSearching()
    # transcript = 'asf'
    # search_query = input("search query: ")
    # asyncio.run(sem_searching.semanticSearch(transcript, search_query))





# ---------------------------------------------------------------------------------------------------------------------------------------------------------




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
#     # driver.quit()  # close browser when DONE


# from webex_spawner import WebexSpawner

# if __name__ == "__main__":
#     # webex spawner - create a chrome instance and spawn a webex meet 
#     spawner = WebexSpawner()
#     spawner.run()


    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
