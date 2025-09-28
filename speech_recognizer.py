# import speech_recognition
import pyttsx3

import subprocess
import speech_recognition as sr

class SpeechRecognition:
   
    # def speech_recognition():
    #     recognizer = speech_recognition.Recognizer()
    #     while True:
    #             try: 
    #                     with speech_recognition.Microphone() as mic:
    #                                 recognizer.adjust_for_ambient_noise(mic, duration=0.2)
    #                                 audio = recognizer.listen(mic)
    #                                 text = recognizer.recognize_azure(audio)
    #                                 text = text.lower()
    #                                 print("recognized : ", text)
    #                     pass
    #             except speech_recognition.UnknownValueError(): 
    #                     recognizer = speech_recognition.Recognizer()
    #                     continue


    def extract_audio(self, video_file, audio_file="audio.wav"):
        # Use ffmpeg to convert video → wav
        command = ["ffmpeg", "-y", "-i", video_file, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_file]
        subprocess.run(command, check=True)
        return audio_file

    def transcribe_audio(self, audio_file):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Load the whole audio

        try:
            text = recognizer.recognize_google(audio)  # Uses Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "❌ Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"⚠️ Could not request results from Google API; {e}"

