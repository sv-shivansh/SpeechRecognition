import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("SAY SOMETHING")
    audio = r.listen(source)
    print("TIME OVER")

try:
    print("text = "+r.recognize_google(audio))
except:
    pass