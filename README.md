
```
# Speech Translation App

This is a Python application that captures spoken language, translates it into another language, and converts the translated text to speech. The application uses the following libraries:
- `googletrans`: A free and unlimited Python library that implements the Google Translate API.
- `speech_recognition`: A library for capturing and recognizing speech.
- `gtts`: Google Text-to-Speech Python library and CLI tool to interface with Google Translate text-to-speech API.
- `playsound`: A simple library for playing sound in Python.

## Features
- Captures spoken language through a microphone.
- Recognizes and converts speech to text.
- Translates the recognized text into a specified target language.
- Converts the translated text to speech.
- Plays the converted speech audio.

## Prerequisites
- Python 3.x
- Install the required libraries using pip:
  ```bash
  pip install googletrans==4.0.0-rc1 speechrecognition gtts playsound
  ```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/speech-translation-app.git
   cd speech-translation-app
   ```

2. **Run the application**:
   ```
   python app.py
   ```

3. **Speak**:
   - When prompted, speak into your microphone.
   - The application will capture your speech, recognize it, translate it to the specified target language, convert the translated text to speech, and play the audio.

## Code Overview

Here's a brief overview of the code in `app.py`:

```
import googletrans  # Googletrans library for translation
import speech_recognition as sr  # Speech recognition library
import gtts  # Google Text-to-Speech library
import playsound  # Library for playing sound

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = googletrans.Translator()

# Define input and output languages
input_lang = 'fr-FR'
output_lang = 'en'

try:
    # Capture speech from the microphone
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        # Recognize the speech using Google recognition
        text = recognizer.recognize_google(voice, language=input_lang)
        print(f"Recognized Text: {text}")

    # Translate the recognized text
    translated = translator.translate(text, dest=output_lang)
    print(f"Translated Text: {translated.text}")

    # Convert the translated text to speech
    converted_audio = gtts.gTTS(translated.text, lang=output_lang)
    converted_audio.save('audio.mp3')

    # Play the converted speech audio
    playsound.playsound('audio.mp3')

except sr.UnknownValueError:
    print("Sorry, I did not understand what you said.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Languages
The application is set up to recognize French (`fr-FR`) and translate it to English (`en`). You can change the `input_lang` and `output_lang` variables to support other languages. For a list of supported languages, refer to the `googletrans` documentation.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Googletrans](https://github.com/ssut/py-googletrans)
- [SpeechRecognition](https://github.com/Uberi/speech_recognition)
- [gTTS](https://github.com/pndurette/gTTS)
- [Playsound](https://github.com/TaylorSMarks/playsound)

