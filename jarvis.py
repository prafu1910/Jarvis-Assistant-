import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser 
#import 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)



def speck(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speck("Good Moring!")

    elif hour>=12 and hour<18:
        speck("Good Aftenoon!")

    else:
        speck("Good Evening!")

    speck("I am Jarvis Sir. Please tell me how may I help you")    

def takeCommand():
    #It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language = 'en-in', show_all=False)  
        print(f"User said: {query}\n")

    except Exception as e:    
        #print(e)
        print("say that again please...")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            pyttsx3.speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            pyttsx3.speak("According to wikipedia")
            print(results)
            speck(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        #elif 'Search' in query: