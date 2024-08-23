import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser


query = None
newquery = None
response = None

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        greet = "Good Morning Sir!"
    elif hour>=12 and hour<18:
        greet = "Good Afternoon Sir!"
    else:
        greet = "Good Evening Sir!"
    send_response(greet + " I am Casper. How can help you?")
    speak(response)



def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)        
            audio = r.listen(source)
        except Exception as e:
            print("Sorry")
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}")

    except Exception as e:
        print(e)
        return "None"
    return query

def question():
    global newquery
    while True:
        f = open("variable.txt", "r")
        f.seek(0)
        if f.read() != "0":
            break   
    f = open("variable.txt", "r+")
    newquery = (f.read().lower())
    f.seek(0)
    f.truncate()
    f.write("0")
    f.close()

def send_response(responsetext):
    global response
    response = responsetext
    r = open("response.txt", "w")
    r.write(response)
    r.close()


#------> Getting Client Command
'''
while True:
                f = open("variable.txt", "r")
                f.seek(0)
                if f.read() != "0":
                    break   
            f = open("variable.txt", "r+")
            query = (f.read())
            f.seek(0)
            f.truncate()
            f.write("0")
            f.close()
'''


turnoffcomputer =['turn off computer', 'turn off the computer', 'shutdown computer', 'turn off my computer', 'shut down my computer', 'turn my computer off', 'turn the computer off']
positive = ['yes', 'sure', 'yea', 'go on']
negative = ['no', 'stop', 'wait', 'never']
calling = ['hello', 'hey casper', 'hey']
good = ['good', 'cool', 'i am good', 'i am cool', 'i am great', 'pretty good', 'super cool', 'i am well', 'feeling good', 'feeling well']
notgood = ['not good', 'not well', 'not feeling good', 'not ok', 'not feeling well']




if __name__ == "__main__":
    greeting()
    while True:
        f = open("variable.txt", "r+")
        query = (f.read().lower())
        f.seek(0)
        f.truncate()
        f.write("0")
        f.close()
        # query = take_command().lower()

        if 'who is' in query:
            query = query.replace("who is", "")
            result = wikipedia.summary(query, sentences=2)
            # speak("According to wikipedia")
            print(result)
            send_response(result)
            speak("According to wikipedia" + response)
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            # speak("According to wikipedia")
            print(result)
            speak("According to wikipedia" + result)
    
        elif 'open youtube' in query:
            send_response("Opening Youtube")
            speak(response)
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            send_response("Opening Google")
            speak(response)
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            send_response("Opening Facebook")
            speak(response)
            webbrowser.open("facebook.com")
        elif 'open a website' in query:
            send_response("Sir, which website should I open?")
            speak (response)
            question()
            send_response(f"Opening {newquery}")
            speak(response)
            webbrowser.open(newquery)
        
        elif any(x in query for x in turnoffcomputer):
            send_response("Sir! Are you sure you want to turn off the computer")
            speak (response)
            # query = take_command().lower()
            question()
            if any(x in newquery for x in positive):
                send_response("Ok Sir, Turning off the computer. Goodbye!")
                speak (response)
                os.system("shutdown /s /t 2")
            elif any(x in newquery for x in negative):
                send_response("Ok Sir")
                speak (response)
        elif 'how are you' in query:
            send_response("I am good as always Sir! How are you?")
            speak(response)
            question()
            # query = take_command().lower()
            if any(x in newquery for x in notgood):
                send_response("Oh, sorry for that. How can I help you?")
                speak(response) 
            elif any(x in newquery for x in good):
                send_response("Cool!! How can I help you?")
                speak(response)
        elif any(x in query for x in calling):
            send_response("Hello Sir! How can I help you?")
            speak(response)
        elif 'are you there' in query:
            send_response("At your service Sir!")
            speak(response)
            
            
        #else :
            #speak("Sorry Sir, I didn't understand what you said. Please say again.")
   
        while True:
            f = open("variable.txt", "r")
            f.seek(0)
            if f.read() != "0":
                break   