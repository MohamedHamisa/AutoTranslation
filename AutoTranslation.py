import googletrans   #Googletrans is a free and unlimited python library that implemented Google Translate API
import speech_recognition as sr
import gtts #Google Text-to-Speech Python library and CLI tool to interface with Google Translate text-to-speech API
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'fr-FR'
output_lang = 'en'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('audio.mp3')
playsound.playsound('audio.mp3')
# print(googletrans.LANGUAGES)  # if you want to print all languages
