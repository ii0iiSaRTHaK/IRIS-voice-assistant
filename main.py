import speech_recognition as sr
import pyaudio
import webbrowser
import pyttsx3
import requests
import google.generativeai as genai
# import threading

headlines_api = "your api key"
gemini_api = "your google api key"


recognizer = sr.Recognizer()
# engine = pyttsx3.init()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine
    

genai.configure(api_key=gemini_api)


gemini_model = genai.GenerativeModel("gemini-2.5-flash")


gemini_chat = gemini_model.start_chat(history=[])


def askgemini(prompt):
    """Send a query to Gemini Flash 2.5 and return the text response."""
    try:
        response = gemini_chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Sorry, I couldn't reach Gemini right now."
    
    
    
    
def opencommand(c):
    if "open google" in c.lower():
        webbrowser.open_new_tab("https://google.com")
    elif "open twitter" in c.lower():
        webbrowser.open_new_tab("https://x.com")
    elif "open insta" in c.lower():
        webbrowser.open_new_tab("https://instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open_new_tab("https://facebook.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open_new_tab("https://Linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open_new_tab("https://youtube.com")
    elif "news" in c.lower():
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={headlines_api}")
        data = req.json()
        titles = [article["title"] for article in data["articles"]]
        for i in titles:
            speak(i)
    else:
        reply = askgemini(c)
        print(f"{reply}")    
        
    
# def speak(text):
#     thread = threading.Thread(target=_speak,args=(text,))
#     thread.start()
    
if __name__ == "__main__":
    speak("initializing jarvis..")
    #Listen for wake word Jarvis
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source,duration=0.5)
                audio = r.listen(source,timeout = 5,phrase_time_limit= 5)
            command = r.recognize_google(audio)
            if "jarvis" in command.lower():
                print("Jarvic Active")
                speak("Yes Mr.Stark")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    opencommand(command);
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected within the limit.")
        except sr.UnknownValueError:
            print("Error: Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Network Error: Could not request results; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
