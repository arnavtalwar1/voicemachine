import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 100)
voice=engine.getProperty('voices')
engine.setProperty('voices', voice[1].id)
# Text to speak
engine.say("Hello Arnav")
engine.say("How r you")

# Run the speech
engine.runAndWait()
