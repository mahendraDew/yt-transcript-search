
# YouTube Video Transcript Search Tool

This is a Python-based tool that makes it easy to search inside YouTube videos and instantly replay the exact moments of interest. With the latest RAG AI search integration, you can now **ask questions and get answers based on the video content itself**.

----------

## Main Features

### 1. RAG AI Search

-   **Retrieve & Generate Answers from Context:** Enter a query, and the tool finds relevant parts of the transcript, extracts context, and generates an answer using RAG (Retrieval-Augmented Generation).
    
-   Useful for deep queries like: _“What did they say about Python libraries?”_ (discussed in the meeting/yt)
    
-   Powered by **LangChain** and **Gemini/LLM embeddings**.
    

### 2. Timestamp Linking

-   Finds exactly where a keyword or phrase is spoken using **fuzzy matching**.
    
-   Opens the downloaded video directly at that timestamp — no need to jump between timestamps.
    

### 3. Semantic Search

-   Understands the **meaning of your query** and finds contextually relevant matches.
    
-   Even if the exact words don’t appear, it can locate answers with similar phrasing or concepts.
    

----------

## How It Works

### Step 1: Download the YouTube Video

`download_video("https://www.youtube.com/watch?v=example")` 

Downloads the video in the best audio+video quality and saves it locally.

### Step 2: Generate Transcript

`transcribe_with_timestamps("downloads/video.mp4")` 

Converts video to audio and generates a transcript with timestamps.

### Step 3: Search & Get Context

#### Keyword Search:
- You can search for a particular keyword or phrase 
`search_transcript(transcript, query="negative indexing")` 

Returns timestamps and snippet of the transcript:

`Found at 01:45 → "Python supports negative indexing..."` 

You can also open the video at that timestamp.

>NOTE: Finds all instances of a keyword or phrase in the transcript using **fuzzy matching**

#### RAG AI Search:
- The tool searches relevant transcript sections and generates a contextual answer.

#### Semantic Search:

-   Finds results even if exact keywords aren’t present.
    
-   Example: Searching for _“AI models”_ can match sentences like _“machine learning systems”_.
    

----------

## Future Enhancements

-   **Video Platform Integration:** This same feature can be implemented in any video recording application, like Webex or MS Teams, allowing users to search through recorded meetings and instantly jump to the exact moments where specific topics were discussed. Additionally, by integrating an LLM, users can ask questions about the meeting content and get contextual answers, effectively “chatting” with the recording to clarify or explore topics in more detail.    
-   Expand RAG AI functionality to handle **full conversational queries** across videos or meetings.
    

----------

## Example Use Case

Imagine a 1-hour YouTube tech talk. Instead of scrubbing through the timeline, just type:

-   **Keyword:** `"machine learning"` → jumps to the exact part.
    
-   **Semantic Search:** `"AI models"` → finds related discussions.
    
-   **RAG Query:** `"Explain LangChain in this video"` → generates a detailed answer from the transcript.
    

----------

## Tech Stack

-   Python 3.10+
    
-   yt-dlp
    
-   ffmpeg
    
-   SpeechRecognition
        
-   LangChain (LLM + RAG + Semantic Search)
    
-   Gemini (LLM Embeddings)
    

----------


##  Quick Setup

- Clone the repo 
``` git clone https://github.com/mahendra-dewangan/yt-transcript-search.git ``` <br/>
``` cd yt-transcript-search ```
- Install dependencies 
``` pip install -r requirements.txt # Run the program python main.py```