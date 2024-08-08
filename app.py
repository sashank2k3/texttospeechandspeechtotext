import streamlit as st
import audiorecorder
import speech_recognition as sr
import pyttsx3

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

st.title("Text-to-Speech and Speech-to-Text App")

st.header("Speech-to-Text")
audio_file = audiorecorder.audio_input("Record your audio:")
if audio_file:
    result = speech_to_text(audio_file)
    st.write(result)

st.header("Text-to-Speech")
user_text = st.text_input("Enter text:")
if st.button("Convert Text to Speech"):
    text_to_speech(user_text)
