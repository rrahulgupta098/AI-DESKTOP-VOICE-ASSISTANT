import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")

    elif  hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening") 
    

speak(" i am jarvis sir please... tell me how may i help you") 
def takeCommand():
    # It take microphone input from the user and return string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        
        print("recognize...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said : {query}\n") 

    except Exception as e:
        
         print(e)

         print("say that again please....")
         return "none"
    return query






if __name__ == "__main__":
     wishme()
     speak(" Hye Sir")
     while True:
         





         


        query = takeCommand().lower()
      

     #logic for exceuting tasks based on query
        if  'wikipedia' in query:

           speak("searching wikipedia...")
           query = query.replace(" wikipedia ","    ")
           results = wikipedia.summary(query ,sentences=3)
           speak("According to wikipedia")
         
         
           print(results)
           speak(results)
           

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\lenovo\\Music'
            songs = os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time in query':
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")
           
    


     
    
    


