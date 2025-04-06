print("starting.....")
print("BEFORE ITS START YOU CAN Ask, what are thing u can do")
print("updated 14.11.2024,     ADD THE NEW FEATURE OF volume max")




#imported lib

import platform
import random
import sys
import webbrowser
from winreg import QueryInfoKey
from httpx import QueryParams
import pyautogui
import pyttsx3
from sklearn.model_selection import RandomizedSearchCV
import speech_recognition as sr
import datetime
import wikipedia
import google
import pywhatkit as wk
import os
import time
import openai
import nltk
import mysql.connector
import spacy
import google
import googlesearch



#voices for HELLO AI 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # voices is set female(1)  ||| for males voices (0)
engine.setProperty('rate', 150)
print("HELLO AI.......")
def speak(audio):
 engine.say(audio)
 engine.runAndWait()


#greetings by time

def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
   speak("Good Morning!")
 elif hour>=12 and hour<18:
  speak("Good Afternoon!")
 else:
  speak("Good Evening!")
 
 speak("SHIVAM SIR! How can I assist you today?")

#query taking 
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source)
    try:
       print("Recognizing...")
       query =r.recognize_google(audio, language='en-in') #HELLO AI languages set to ENGLISH
       print(f"USER said: {query}\n")   


    except Exception as e:
       print("Say that again ...")
       speak
       return "None"
    return query



# DATABASE SQL


def get_contact_info(query):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="typezero0",
        database="mydatabase"
    )
    mycursor = mydb.cursor()

    # Extract the contact name from the query, e.g., "contact details of Shivam"
    name = query.replace("contact details of", "").strip().lower()

    # Case-insensitive search for contact in database
    sql_query = "SELECT * FROM contacts WHERE lower(lower_name) = %s OR lower(lower_name1) = %s"
    mycursor.execute(sql_query, (name, name))
    myresult = mycursor.fetchone()

    if myresult:
        name, phone = myresult[0], myresult[1]
        contact_info = f"Name: {name}, Phone: {phone}"
        print(contact_info)
        speak(contact_info)  # Speak the contact details
    else:
        print("Contact not found.")
        speak("Contact not found.")

    mydb.close()      
        
    
if __name__=="__main__":
   wishMe()
   while True:
      query = takecommand().lower()
      if 'hello' in query:
         print("YES SIR")
         speak("YES SIR")
      if query and 'contact details of' in query:  # Check if the command is asking for contact details
            get_contact_info(query)
      if 'what you can do for me' in query:
        print("Greetings! I'm here to assist you in various ways. Here are some of the things I can do for you:")
        print("\nConversational Interaction:")
        print("- Engage in friendly conversations and respond to your queries.")
        print("\nInformation Retrieval:")
        print("- Provide information by searching Wikipedia. Just ask 'What is' or 'Who is.'")
        print("\nWeb Browsing:")
        print("- Open Google or YouTube, perform searches, and even play your favorite songs.")
        print("\nApplication and Window Control:")
        print("- Manage applications like Microsoft Word, Google Chrome, and more. I can open, close, and control windows.")
        print("\nSystem Operations:")
        print("- Execute system operations like shutting down, restarting, or putting the system to sleep.")
        print("\nVolume Control:")
        print("- Adjust the system volume to your liking—whether it's increasing, decreasing, or muting.")
        print("\nMiscellaneous Actions:")
        print("- Open Notepad, write notes, play songs, provide the current time, and refresh the screen.")
        print("\nWeb Search:")
        print("- Conduct Google and YouTube searches based on your queries.")
        print("\nVoice Interaction:")
        print("\nFeel free to ask me anything or request assistance with tasks. I'm here to make things easier for you!")
        print("- Respond to voice commands, making our interaction more natural and enjoyable.")
        speak("I'm here to assist you in various ways. YOU CAN READ BELOW. ELSE CAN I READ FOR YOU?")
      elif 'read' in query:
        speak("Greetings! I'm here to assist you in various ways. Here are some of the things I can do for you:")
        speak("\nConversational Interaction:")
        speak("- Engage in friendly conversations and respond to your queries.")
        speak("\nInformation Retrieval:")
        speak("- Provide information by searching Wikipedia. Just ask 'What is' or 'Who is.'")
        speak("\nWeb Browsing:")
        speak("- Open Google or YouTube, perform searches, and even play your favorite songs.")
        speak("\nApplication and Window Control:")
        speak("- Manage applications like Microsoft Word, Google Chrome, and more. I can open, close, and control windows.")
        speak("\nSystem Operations:")
        speak("- Execute system operations like shutting down, restarting, or putting the system to sleep.")
        speak("\nVolume Control:")
        speak("- Adjust the system volume to your liking—whether it's increasing, decreasing, or muting.")
        speak("\nMiscellaneous Actions:")
        speak("- Open Notepad, write notes, play songs, provide the current time, and refresh the screen.")
        speak("\nWeb Search:")
        speak("- Conduct Google and YouTube searches based on your queries.")
        speak("\nVoice Interaction:")
        speak("- Respond to voice commands, making our interaction more natural and enjoyable.")
        speak("\nFeel free to ask me anything or request assistance with tasks. I'm here to make things easier for you!")

            
      
      elif "who are you" in query:
        print('My Name Is HELLO')
        speak('My Name Is HELLO')
        print('I can Do Everything that my creator programmed me to do')
        speak('I can Do Everything that my creator programmed me to do')

      elif "who created you" in query:
        print('His Name SHIVAM , HE  created ME  with Python Language, in Visual Studio Code.')
        speak('His Name SHIVAM , HE created ME with  Python Language, in Visual Studio Code.') 
       
        
      
      elif 'what is' in query:
        speak('Searching Wikipedia...')
        query = query.replace("what is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
      elif 'who is' in query:
        speak('Searching Wikipedia...')
        query = query.replace("who is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
      elif 'auto search on' in query:
             speak("Auto search is on. I will search for you on the web.")
             os.startfile('C:/Users/91701/Desktop/autoclickserch.py')
      elif 'auto search off' in query:
        os.system("taskkill /f /im Python")  
        
        
        #opeing application code
     
      elif 'just open google' in query:
        webbrowser.open("google.com")
        

      elif 'search on google' in query:
        #speak("should i search anything for you?")
      #   qry = takecommand().lower()
      #   webbrowser.open(f"{qry}")
        query = query.replace("search on google","")
        webbrowser.open(f"https://www.google.com/search?q={query}")     
      #   results = wikipedia.summary(   qry, sentences=1)
      #   speak(results)
      #   erro for this open google is not working want to check it out later
        
      elif 'just open youtube' in query:
        webbrowser.open("youtube.com") 

      elif 'open youtube' in query:
        # qrry = takecommand().lower()
        wk.playonyt(f"{query}") 

      elif 'search on YouTube' in query:
        query = takecommand().lower()
        query = query.replace("search on YouTube","")
        webbrowser.open(f"www.youtube.com/results?search_query={query}")


      elif "open Word".lower() in query.lower():
            print("AI...")
            # Check the platform to determine the command to open Microsoft Word
            if platform.system() == "Windows":
                os.system("start winword")
                speak("Opening Microsoft Word for you sir.")


#closing code for application or web
      elif ' close Chrome' in query:
        os.system("taskkill /f /im chrome.exe") 
        speak("ok sir")  
      elif 'close chrome' in query:
        os.system("taskkill /f /im chrome.exe")      
      elif 'close edge' in query:
        os.system("taskkill /f /im msedge.exe") 
      elif 'hacker mod on'in query:
              os.startfile('C:/Program Files/eDEX-UI/eDEX-UI.exe') 
              speak('HACKER MODE HAD BEEN ON.And now I am switching off. Have a safe hacking shivam')
              sys.exit() 
      elif 'play song' in query:
        music_dir = "C:/Users/91701/Music/hindi song"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
      elif "time".lower() in query.lower():
            print("AI...")
            speak("sir time is..")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)   
      elif "shutdown the system" in query:
         speak("ok bye sir see  you soon....")
         os.system("shutdown /s /t  5")
      elif "restart the system" in query:
         os.system("shutdown /r /t 5")
      elif "Lock the system" in query:
         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    
      elif "lock the system" in query:
         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
      elif "go to sleep" in query:
         speak(' alright then, I am switching off')
         sys.exit()
      elif "volume up" in query:
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")

      elif "volume down" in query:
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       pyautogui.press("volumedown")
       
      elif "volume max" in query:
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
       pyautogui.press("volumeup")
      
      elif "mute" in query:
       pyautogui.press("volumemute")
      elif "unmute" in query:
        pyautogui.press("volumemute")
      
      elif "refresh" in query:
       pyautogui.moveTo(1551,551, 2)
       pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
       pyautogui.moveTo(1620,667, 1)
       pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
       if "refresh two" in query:
        pyautogui.moveTo(1551,551, 2)
        pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
        pyautogui.moveTo(1620,667, 1)
        pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        pyautogui.moveTo(1551,551, 2)
        pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
        pyautogui.moveTo(1620,667, 1)
        pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        speak("done")
      elif "scroll down" in query:
       pyautogui.scroll(1000)  
      elif "open notepad and write anything" in query:
       pyautogui.hotkey('win')
       time.sleep(1)
       pyautogui.write('notepad')
       time.sleep(1)
       pyautogui.press('enter')
       time.sleep(1)
       pyautogui.write("hello friends i am hello,shivam is my friend", interval = 0.1)  
      if 'open chrome' in query:
       os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
      elif 'maximize this window' in query:
       pyautogui.hotkey('alt', 'space')
       time.sleep(1)
       pyautogui.press('x')
      elif 'google search' in query:
       query = query.replace("google search", "")
       pyautogui.hotkey('alt', 'd')
       pyautogui.write(f"{query}", 0.1)
       pyautogui.press('enter')
      elif 'youtube search' in query:
       query = query.replace("youtube search", "")
       pyautogui.hotkey('alt', 'd')
       time.sleep(1)
       pyautogui.press('tab')
       pyautogui.press('tab')
       pyautogui.press('tab')
       pyautogui.press('tab')
       time.sleep(1)
       pyautogui.write(f"{query}", 0.1)
       pyautogui.press('enter')
      elif 'close this window' in query:
              pyautogui.hotkey('ctrl', 'f4') 
      elif 'open new window' in query:
              pyautogui.hotkey('ctrl', 'n')
      elif 'open incognito window' in query:
              pyautogui.hotkey('ctrl', 'shift', 'n')
      elif 'minimise this window' in query:
              pyautogui.hotkey('alt', 'space')
              time.sleep(1)
              pyautogui.press('n')
      elif 'open history' in query:
              pyautogui.hotkey('ctrl', 'h')
      elif 'open downloads' in query:
              pyautogui.hotkey('ctrl', 'j')
      elif 'previous tab' in query:
              pyautogui.hotkey('ctrl', 'shift', 'tab')
      elif 'next tab' in query:
              pyautogui.hotkey('ctrl', 'tab')
      elif 'close tab' in query:
              pyautogui.hotkey('ctrl', 'w')
      elif 'close window' in query:
              pyautogui.hotkey('ctrl', 'shift', 'w')
      elif 'clear browsing history' in query:
              pyautogui.hotkey('ctrl', 'shift', 'delete')
      elif 'close chrome' in query:
              os.system("taskkill /f /im chrome.exe")
      elif  "your name" == query or "who are you" == query:
         speak("I am an AI assistant NAME HELLO.")
      elif  "how are you" in query:
         speak("I AM FINE,DOING WELL,WHAT ABOUT YOU? ANYTHING THERE THAT I CAN HELP YOU?") 
      elif 'open file manager' in query:
              pyautogui.hotkey('win', 'e')
              # pyautogui.write("cmd", interval = 0.1)
              # pyautogui.press('enter')
      elif 'open command' in query:
              pyautogui.hotkey('win', 'r')
              pyautogui.write("cmd", interval = 0.1)
              pyautogui.press('enter')
      elif 'open vs code' in query:
              pyautogui.hotkey('win', '3') 
      elif 'open whatsapp' in query:
              pyautogui.hotkey('win', '7') 
      elif 'go to home' in query:
              pyautogui.hotkey('win', 'd') 
      
      elif 'put system to sleep' in query:
          pyautogui.hotkey('win','x',interval=0.2)
          pyautogui.hotkey('u','s')   
      
      
      
      
      
      
      
      elif "open database" in query:
          pyautogui.hotkey('win','r')
          time.sleep(1)
          pyautogui.write('cmd')
          time.sleep(1)
          pyautogui.press('enter')
          time.sleep(1)
          pyautogui.write("mysql -u root -p", interval = 0.1)
          pyautogui.press('enter')
          time.sleep(1)
          pyautogui.write("typezero0",)
          pyautogui.press('enter')
          pyautogui.write("use mydatabase;")
          pyautogui.press('enter')
          pyautogui.press('enter')
          pyautogui.write("select * from contacts;")
          pyautogui.press('enter')
          
      elif "close database" in query:
          pyautogui.hotkey('ctrl','z')
          pyautogui.press('enter')
          pyautogui.write("exit")
          pyautogui.press('enter')
          
          
      elif "restart yourself" in query:
          os.startfile( 'C:/Users/91701/Desktop/HELLO AI.py')
          sys.exit()
          
          
          
          
        
       
       
       
             
       
       
      # os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')   
   

# import requests

# def get_weather(city):
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": weather_api_key,
#         "units": "metric"  # You can change the units to imperial for Fahrenheit
#     }
#     response = requests.get(base_url, params=params)
#     weather_data = response.json()

#     if response.status_code == 200:
#         temperature = weather_data["main"]["temp"]
#         weather_description = weather_data["weather"][0]["description"]
#         return f"The temperature in {city} is {temperature}°C with {weather_description}."
        
#     else:
#         return "Unable to fetch weather information. Please try again later."

# def main():
#     wishMe()
#     while True:
#         query = takecommand().lower()

#         if 'weather' in query:
#             city = query.split('in')[-1].strip()
#             weather_info = get_weather(city)
#             speak(weather_info)   

                                   




