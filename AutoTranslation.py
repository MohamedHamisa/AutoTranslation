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
