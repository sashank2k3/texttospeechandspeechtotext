import streamlit as st
import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr
import pyttsx3
import io

# Record audio using sounddevice
def record_audio(duration=5, samplerate=44100):
    st.write("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    st.write("Recording complete")
    return audio_data, samplerate

# Convert audio to text
def audio_to_text(audio_data, samplerate):
    recognizer = sr.Recognizer()
    audio_file = io.BytesIO()
    wavio.write(audio_file, audio_data, samplerate, sampwidth=2)
    audio_file.seek(0)
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

st.title("Text-to-Speech and Speech-to-Text App")

st.header("Speech-to-Text")
if st.button("Record Audio"):
    audio_data, samplerate = record_audio()
    result = audio_to_text(audio_data, samplerate)
    st.write(result)

st.header("Text-to-Speech")
user_text = st.text_input("Enter text:")
if st.button("Convert Text to Speech"):
    text_to_speech(user_text)
