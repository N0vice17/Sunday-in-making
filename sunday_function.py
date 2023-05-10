from jokeapi import Jokes
import speech_recognition as sr
from datetime import datetime
from win32com.client import Dispatch
import webbrowser
import requests
import json
import os
import smtplib
import pywhatkit

with open("Sunday.json") as file:
    sunday_file = json.load(file)["Personal_Details"]


def sunday_string(str):
    print(f"Sunday:{str}")


def sunday_speak(str):
    speak = Dispatch("SAPI.spvoice")
    speak.Speak(str)


def sunday_welcome():
    sunday_speak("Warming up the system")
    sunday_speak("Sunday is Online")
    sunday_string("Welcome To Your System " + sunday_file["Admin_name"])
    sunday_speak("Welcome To Your System" + sunday_file["Admin_name"])
    time = datetime.now().hour
    if 0 <= time <= 12:
        sunday_string("Good Morning")
        sunday_speak("Good Morning")
    elif 12 < time <= 16:
        sunday_string("Good Afternoon")
        sunday_speak("Good Afternoon")
    else:
        sunday_string("Good Evening")
        sunday_speak("Good Evening")


async def sunday_joke():
    Initialising = await Jokes()
    Joke = await Initialising.get_joke(category=['dark'])
    if Joke["type"] == "single":
        sunday_string(Joke["joke"])
        sunday_speak(Joke["joke"])
    else:
        sunday_string(Joke["setup"])
        sunday_speak(Joke["setup"])
        sunday_string(Joke["delivery"])
        sunday_speak(Joke["delivery"])


def sunday_recognise():
    Recognising = sr.Recognizer()
    with sr.Microphone(0) as source:
        sunday_string("I am Listening")
        audio = Recognising.listen(source)
    try:
        Statement = Recognising.recognize_google(audio, language="en-Us")
        print(f"You said:{Statement}")
    except Exception:
        return "Speech Recognition not working properly"
    return Statement


def sunday_browseropening(str):
    sunday_string(f"Opening {str}")
    sunday_speak(f"Opening {str}")
    webbrowser.open(f"{str}.com")


def sunday_newsreader():
    Request = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=a5f600e382764c839aa0b26146f62d75")
    Text = Request.text
    String = json.loads(Text)
    News = (String["articles"])
    for articles in News:
        sunday_speak(articles["title"])


def sunday_playmusic():
    Path = "D:\\songs"
    songs = os.listdir(Path)
    os.startfile(os.path.join(Path, songs[0]))


def sunday_sendmail():
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    sunday_string("Enter Email id and password of sender")
    sunday_speak("Enter Email id and password of sender")
    email = input("Email:")
    password = input("Password:")
    mail.login(f"{email}", f"{password}")
    sunday_string("Enter email of the recipient")
    sunday_speak("Enter the id of the recipient")
    receiver = input("Email:")
    sunday_string("Subject Here")
    sunday_speak("Subject Here")
    subject = input()
    mail.sendmail(f"{email}", f"{receiver}", f"{subject}")
    mail.quit()


def sunday_time():
    time = datetime.now().strftime("%H,%M,%S")
    sunday_string(time)
    sunday_speak(time)


def sunday_weather():
    Requests = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?lat=22.569&lon=88.369&appid=28ff755dcb874b7205d0ed23718fff22")
    Text = Requests.text
    String = json.loads(Text)
    Current_Weather = String["weather"]
    for weather in Current_Weather:
        a = (weather["main"])
        sunday_string(f"Today's Weather is {a}")
        sunday_speak(f"Today's Weather is {a}")
    Name = String["name"]
    sunday_string(f"You are in {Name}")
    sunday_speak(f"You are in {Name}")
    Main = String["main"]
    Temparature = Main["temp"]
    temp = int(Temparature - 273)
    Humidity = Main["humidity"]
    sunday_string(f"The temparature in {Name} is {temp} Degree Celcius and Humidity is {Humidity}")
    sunday_speak(f"The temparature in {Name} is {temp} Degree Celcius and Humidity is {Humidity}")


def sunday_sendmessage_whatsapp_group():
    sunday_string("Group Name:")
    sunday_speak("Group Name")
    name = input()
    sunday_string("Message:")
    sunday_speak("Message")
    Message = input()
    pywhatkit.sendwhatmsg_to_group_instantly(f"{name}", f"{Message}")
    sunday_speak("Message has been sent")


def sunday_sendmessage_whatsapp_contact():
    sunday_string("Phone number:")
    sunday_speak("Phone number")
    Number = input()
    sunday_string("Message:")
    sunday_speak("Message")
    Message = input()
    pywhatkit.sendwhatmsg_instantly(f"{Number}", f"{Message}")
    sunday_speak("Message has been sent")
