import uuid
import os
import time
import speech_recognition as sr
import playsound
import speech_recognition as sr
from gtts import gTTS


# Function for Listening Audio
def listenAudio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak Anything :")
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			print("You said : {}".format(text))
		except:
			print("Sorry could not recognize what you said")
	return text

# Function for Making our Assistant speak (Covert I/P Text To Speech)
def speak(text):
    
    # creating an gTTS Object
    textToSpeech = gTTS(text = text, lang = 'en')
    
    filename = str(uuid.uuid4()) + '.mp3'
    
    # saving the voice clip
    textToSpeech.save(filename)
    
    # play the voice clip
    playsound.playsound(filename)

text = listenAudio()
if "hello" in text:
	speak('Hi Friend, Doing good! What about you?')

    
