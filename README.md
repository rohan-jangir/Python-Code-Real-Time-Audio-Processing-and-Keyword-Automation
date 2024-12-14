# Real-Time Audio Processing and Automation

This project combines real-time audio transcription using OpenAI's Whisper model with web automation powered by Selenium. It records audio, transcribes it, and performs automated browser actions based on detected keywords.

## Features

- **Real-Time Audio Recording**: Captures audio input using PyAudio.
- **AI-Powered Transcription**: Utilizes the Whisper model for accurate speech-to-text conversion.
- **Keyword Detection**: Matches specific keywords in the transcribed text.
- **Web Automation**: Automates browser navigation with Selenium based on detected keywords.
- **Customizable Settings**: Adjustable silence thresholds, recording durations, and keywords.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.8 or higher
- Libraries:
  - `whisper`
  - `pyaudio`
  - `wave`
  - `tempfile`
  - `numpy`
  - `selenium`
  - `os`
  - `re`
- A Selenium WebDriver (e.g., EdgeDriver, ChromeDriver).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/real-time-audio-automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd real-time-audio-automation
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your microphone is connected and functional.
2. Run the script:
   ```bash
   python main.py
   ```
3. Speak into the microphone. The program will:
   - Transcribe your speech in real-time.
   - Detect specified keywords (e.g., Google, YouTube).
   - Open the corresponding website in a browser if a keyword is detected.

## Configuration

- Modify the following parameters in the code as needed:
  - `SILENCE_THRESHOLD`: Amplitude threshold for detecting silence.
  - `SILENCE_LIMIT`: Duration (in seconds) of silence to stop recording.
  - `keywords`: List of keywords to match in the transcription.

## Example

1. Say "Open Google".
2. The program transcribes your speech and detects the keyword "Google".
3. Selenium launches a browser and navigates to `https://www.google.com`.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Acknowledgements

- **OpenAI Whisper**: For providing a robust transcription model.
- **Selenium**: For seamless browser automation.
- **PyAudio**: For real-time audio processing.

---

Happy coding! 🚀
