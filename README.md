
# YouTube Video Transcript Search Tool

This project is a Python-based tool that makes it easy to **search for any phrase inside a YouTube video** and **instantly replay** the exact part where it’s discussed.

It downloads a YouTube video, extracts its transcript using speech recognition, and allows you to search for keywords or perform **semantic searches**. The program then returns the **timestamp** and a **direct link** to that moment in the downloaded video.

----------

##  Features

-   **YouTube Video Downloader** – Downloads videos with audio using `yt-dlp` and `ffmpeg`.
    
-   **Automatic Transcription** – Converts video to audio and generates a text transcript with timestamps using `SpeechRecognition`.
    
-   **Keyword & Semantic Search** – Search for exact keywords or use **semantic search** to find related phrases and meanings using embeddings.
    
-   **Timestamp Linking** – Opens the downloaded video directly at the moment where the phrase is spoken.
    
-   **AI Integration (Future Scope)** – Can be enhanced with LLMs to enable conversational queries such as “What did they say about X?” — basically, _chat with your video_.
    

----------

##  Tech Stack

-   **Python 3.10+**
    
-   [yt-dlp](https://github.com/yt-dlp/yt-dlp?utm_source=chatgpt.com)
    
-   [ffmpeg](https://ffmpeg.org/)
    
-   [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
    
-   [pydub](https://pypi.org/project/pydub/)
    
-   LangChain – for LLM and **semantic search**
       

----------

##  How It Works

###  Step 1: Download the YouTube Video

`download_video("https://www.youtube.com/watch?v=example")` 

Downloads the video with best audio + video quality and merges them into a single `.mp4` file.

----------

###  Step 2: Generate Transcript

`transcribe_with_timestamps("downloads/video.mp4")` 

Converts the video to audio and transcribes it into text chunks with timestamps.

----------

###  Step 3: Search the Transcript

`search_transcript(transcript, query="negative indexing")` 

Finds all instances where the phrase appears and returns:

`Found at 01:45 → "Python supports negative indexing..."` 

You can also open the local video at that timestamp.

----------

###  Step 4: Perform Semantic Search

In addition to keyword matching, the program supports **semantic search** using embeddings.  
This means it can find results **even if the exact words don’t match** — for example, searching for  
“AI models” will still match sentences containing “machine learning systems.”

----------

##  Future Enhancements
    
-   Implement a **Webex meeting** version — allowing users to search and replay exact discussion points in recorded meetings.
    
    

----------

##  Example Use Case

> Imagine watching a 1-hour tech talk on YouTube — instead of scrubbing through the timeline, just type  
> **“machine learning”**, and jump straight to the part where it’s mentioned.  
> You can even perform **semantic searches** like “AI models” or “neural networks” to find related discussions.

----------

##  Quick Setup

- Clone the repo 
``` git clone https://github.com/mahendra-dewangan/yt-transcript-search.git ``` <br/>
``` cd yt-transcript-search ```
- Install dependencies 
``` pip install -r requirements.txt # Run the program python main.py```
