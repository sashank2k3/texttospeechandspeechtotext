import streamlit as st
import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
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
if st.button("Convert Speech to Text"):
    result = speech_to_text()
    st.write(result)

st.header("Text-to-Speech")
user_text = st.text_input("Enter text:")
if st.button("Convert Text to Speech"):
    text_to_speech(user_text)
