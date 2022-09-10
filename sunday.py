import sunday_function
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import json
import asyncio

with open("sunday.json") as file:
    sunday_file = json.load(file)["Personal_Details"]
if __name__ == "__main__":
    while True:
        Recognising = sr.Recognizer()
        with sr.Microphone(0) as source:
            audio = Recognising.listen(source)
            statement = Recognising.recognize_google(audio, language="en-Us")
            if "up" in statement:
                sunday_function.sunday_welcome()
                sunday_function.sunday_weather()
                while True:
                    Statement = sunday_function.sunday_recognise().lower()
                    if "wikipedia" in Statement:
                        try:
                            statement = Statement.replace("wikipedia", "")
                            summary = wikipedia.summary(statement, sentences=3)
                            sunday_function.sunday_string(summary)
                            sunday_function.sunday_speak(summary)
                        except Exception as e:
                            sunday_function.sunday_string("This Page is not found")
                            sunday_function.sunday_speak("This Page is not found")
                    elif "created" in Statement:
                        sunday_function.sunday_string(
                            "I am Created by Debojit Ganguly in the month of April. He created me on an evening of "
                            "sunday")
                        sunday_function.sunday_speak(
                            "I am Created by Debojit Ganguly in the month of April. He created me on an evening of "
                            "sunday")
                    elif "Debojit" in Statement:
                        sunday_function.sunday_string(sunday_file["About"])
                        sunday_function.sunday_speak(sunday_file["About"])
                    elif "contact" in Statement:
                        sunday_function.sunday_sendmessage_whatsapp_contact()
                    elif "send message" in Statement:
                        sunday_function.sunday_sendmessage_whatsapp_group()
                    elif "open whatsapp" in Statement:
                        os.startfile("C:\\Users\\Debojit Ganguly\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
                    elif "time" in Statement:
                        sunday_function.sunday_time()
                    elif "mail" in Statement:
                        sunday_function.sunday_sendmail()
                    elif "news" in Statement:
                        sunday_function.sunday_newsreader()
                    elif "play music" in Statement:
                        sunday_function.sunday_playmusic()
                    elif "youtube " in Statement:
                        webbrowser.open("youtube")
                    elif "github" in Statement:
                        webbrowser.open(sunday_file["Github"])
                    elif "google" in Statement:
                        sunday_function.sunday_browseropening("google")
                    elif "stackoverflow" in Statement:
                        sunday_function.sunday_browseropening("stackoverflow")
                    elif "twitter" in Statement:
                        webbrowser.open(sunday_file["Twitter"])
                    elif "facebook" in Statement:
                        sunday_function.sunday_browseropening("facebook")
                    elif "linkedin" in Statement:
                        webbrowser.open(sunday_file["Linkedin"])
                    elif "calculator" in Statement:
                        os.startfile("D:\\Pycharm Projects\\calculator.exe")
                    elif "joke" in Statement:
                        asyncio.run(sunday_function.sunday_joke())
                    elif "shutdown" in Statement:
                        sunday_function.sunday_speak("Shutting Down")
                        exit()
                    else:
                        sunday_function.sunday_speak("I cant hear you")
            else:
                sunday_function.sunday_string("I Cant Hear you")
