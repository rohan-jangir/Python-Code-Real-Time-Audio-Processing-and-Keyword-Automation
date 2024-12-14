import whisper
import pyaudio
import wave
import tempfile
import numpy as np
import time
from selenium import webdriver
import os
import re

# Load Whisper model
model = whisper.load_model("base")

# PyAudio setup
SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_SIZE = 1024
SILENCE_THRESHOLD = 500  # Silence threshold for detecting pause (in amplitude)
SILENCE_LIMIT = 3  # Silence limit (seconds) to stop recording

# Function to record and transcribe audio
def record_and_transcribe(max_duration=60):
    print("Starting audio recording...")

    # Setup PyAudio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=CHANNELS, rate=SAMPLE_RATE, input=True, frames_per_buffer=CHUNK_SIZE)
    
    frames = []
    last_speech_time = time.time()  # Track the last time speech was detected
    recording = True  # Flag to indicate if we're still recording

    while recording:
        data = stream.read(CHUNK_SIZE)
        frames.append(data)
        
        # Convert the audio data to numpy array for silence detection
        audio_data = np.frombuffer(data, dtype=np.int16)
        silence = np.max(np.abs(audio_data)) < SILENCE_THRESHOLD
        
        if silence:
            if time.time() - last_speech_time >= SILENCE_LIMIT:
                recording = False  # Stop recording after 3 seconds of silence
        else:
            last_speech_time = time.time()  # Reset the silence timer when speech is detected
    
    # Stop the stream and process the recording
    print("Recording complete.")
    stream.stop_stream()
    stream.close()
    
    # Save the frames to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        with wave.open(temp_file.name, "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(b"".join(frames))

        print("Transcribing audio...")
        # Transcribe the recorded audio
        result = model.transcribe(temp_file.name)
        
        print(f"Transcription result: {result['text']}")  # Print the transcription result for debugging

        # List of keywords to check in the transcription
        keywords = ["Google", "YouTube", "Facebook", "Instagram"]
        
        # Extract matching keywords from the transcription text
        matches = []
        for word in keywords:
            # Clean up the word and result text (remove spaces and non-alphanumeric characters)
            clean_word = re.sub(r'\W+', '', word.lower())
            clean_text = re.sub(r'\W+', '', result['text'].lower())
            if clean_word in clean_text:
                matches.append(word)

        if matches:
            # Initialize Selenium WebDriver only if there are matches
            driver = webdriver.Edge()
            keyword = matches[0]  # Use the first matching keyword
            print(f"Opening: https://www.{keyword}.com")
            driver.get(f'https://www.{keyword}.com/')
        else:
            print("No valid keyword extracted.")
    
    os.remove(temp_file.name)  # Clean up the temporary file

# Example usage
record_and_transcribe(max_duration=60)
