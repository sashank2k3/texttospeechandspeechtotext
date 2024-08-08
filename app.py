import streamlit as st
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import io

def record_audio(duration=5, fs=44100):
    st.write("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    st.write("Recording finished")
    return recording

def speech_to_text(recording):
    recognizer = sr.Recognizer()
    with io.BytesIO(recording.tobytes()) as audio_buffer:
        audio_buffer.seek(0)
        try:
            audio = sr.AudioFile(audio_buffer)
            with audio as source:
                audio_data = recognizer.record(source)
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
if st.button("Convert Speech to Text"):
    recording = record_audio()
    result = speech_to_text(recording)
    st.write(result)

st.header("Text-to-Speech")
user_text = st.text_input("Enter text:")
if st.button("Convert Text to Speech"):
    text_to_speech(user_text)
