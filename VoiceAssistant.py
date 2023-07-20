
import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import time 
import wolframalpha
import subprocess
import requests
import pyjokes
import pyaudio





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print (voices)
engine.setProperty('voice',voices[1].id)
user=""


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def takecommand():#takes input from microphone and gives string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print ("Listening.....")
         r.pause_threshold=1.5
         #r.adjust_for_ambient_noise(source)
         audio= r.listen(source)
        
    try:
        query= r.recognize_google(audio,language='en-in')
        #print(f"User said: {query}\n")
        speak("You said "+query)

    except Exception as e:
        speak ("Say that again please....")
        return "None"
    return query


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Goodmorning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening ")
    speak(user)
    speak("How may I help you?")

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

OPENWEATHER_APP_ID = ("eccef0646da92a1712398c5211e2f9cb")


def get_weather_report(city):
    res = requests.get(
        #f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={eccef0646da92a1712398c5211e2f9cb}&units=metric").json()
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

NEWS_API_KEY = ("45511997aafd430092f95b8a8953cbd9")

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def verify():
    for i in range(0,3):
        speak("Please share your name and passcode")
        
        query=takecommand().lower()
    
        if "roshan" in query and "115" in query:        
            return True
        elif "feni" in query and "121" in query:   
            return True
        elif "tanishq" in query and "116" in query:   
            return True
        elif "akash" in query and "10" in query:   
            return True
        if i<2:
            speak("please repeat")
    return False

   
if __name__=="__main__":
    
    auth=verify()
    if auth==True:
        #If the user is verifed then 
        
        wishme()
        while True:
            query=takecommand().lower()
            if 'terminate'in query or "stop" in query:
                exit()

                # creating different tasks 
            if 'wikipedia'in query:
                speak("Searching Wikipedia")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                
                #print(results)
                speak ("According to Wikipedia")
                speak (results)


            elif 'search google' in query: #Searching google  
                speak('What should I search google for?')
                s=takecommand().lower()
                speak('Opening Google') 
                pywhatkit.search(s)
                time.sleep(10)
                

        
            elif 'the time' in query:#Speaking the time
                strTime = datetime.datetime.now().strftime("%I:%M %p")    
                speak(f"the time is {strTime}")

            elif 'tell me' in query:
                while(1):
                    speak('Ask me anything')
                    question=takecommand()
                    if'exit' in question:
                        break

                    client = wolframalpha.Client('J9EYYX-VRRWEY9TG7')
                    
                    try :
                        res = client.query(question)

                        answer = next(res.results).text
                        speak(answer)
                    except Exception:
                        speak('Say that again please')

                
            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing ')
                pywhatkit.playonyt(song)
                time.sleep(15)
            
            elif 'whatsapp' in query:
                pywhatkit.open_web()
                time.sleep(15)
            
            elif 'weather' in query:
                
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it ")

            elif 'news' in query:
                speak(f"I'm reading out the latest news headlines, sir")
                speak(get_latest_news())
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_latest_news(), sep='\n')

            elif "joke" in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)
            

            elif 'open webcam' in query:
                codePath2 = "C:\Program Files (x86)\camlife\camlife.exe"
                os.startfile(codePath2)
        
            elif 'log off' in query or 'sign out' in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

    else:
        speak("Invalid credentials ")
        exit()
