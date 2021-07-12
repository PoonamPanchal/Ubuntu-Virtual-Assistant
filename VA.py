import sys
import speech_recognition as sr
import pyttsx3
import re
from datetime import date,datetime
from pyowm.owm import OWM
import os
import webbrowser
import smtplib
import wikipedia



engine = pyttsx3.init()


#What can I do
def What_I_do():
    print("I can send mail ,command me : send mail")
    print("I can search querry on google, command me : search or google")
    print("I can open browser ,command me:open browser or default browser or firefox")
    print("I can open terminal")
    print("I can open libreoffice draw,command me : open draw or wanna paint")
    print("I can open libreoffice calc,command me : open excel or open calc or spreadsheet")
    print("I can open libreoffice writer,command me : open writer")
    print("I can open terminal,command me : open terminal or terminal")
    print("I can shutdown pc,command me : shutdown")
    print("I can tell weather conditions,command me : weather or temperature")
    print("I can open youtube say me open youtube or search youtube")
    print("I can tell you today's day : command me : tell day")
    print("I can tell you current time : command me : tell me time or current time or what is the time")
    print("I can tell you todays date : command me : todays date or tell me date")
    print("I can open text editor,command me open text editor")
    print("I can shutdown your computer say me shutdown ")
    print("I can tell you about what I can do, command me :What can you do")
    print("I can tell you about my self, command me :about youself or your name or who are you")
    print("I can open visual studio command,command me: open visual studio code")
                      
# List of Commands
#Get Date ****************
def get_date():
    today = date.today()
    current_date = today.strftime("%B %d, %Y")
    return current_date
#________________Get TIME ___________
def get_time():
    print("called")
    current_time=datetime.now()
    return current_time

    

#Get Weather/Temperature
def show_weather(city):
    api_key="68388d63e25488334f90cadb33c0f4a4"
    owm=OWM(api_key)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city) 
    weather=observation.weather
    temp=weather.temperature(unit='celsius')
    print(weather)
    
    print ("Average Temp. Currently ", temp['temp']) # get avg. tmp
    print("Detailed Status:",weather.detailed_status)
    return temp['temp'],weather.status

#Shutdown pc           
def system_shutdown():
    os.system("shutdown now -h")
    return
            
def search_google():
    engine.say("input your query")
    engine.runAndWait()
    query=input("Wtite your query")

    webbrowser.open('https://google.com/search?q=%s' % query)
    return
    



def recognize_speech_from_mic(recognizer, microphone):
    

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

   
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:

        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
      
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
       
        response["error"] = "Unable to recognize speech"
    
    return response

def bye():
    exit()


def Query():
    current_date=get_date()
    current_time=get_time()
    current_hour=int(current_time.strftime("%H"))
    engine.setProperty('voice','english_rb+f3')
    if current_hour<12:
        engine.say("Good Morning friend I am your virtual Assistant. How can I help you? ")
        print("Good Morning friend I am your virtual Assistant. How can I help you? ")

    elif 12>=current_hour<18:
        engine.say("Good afternoon friend I am your virtual Assistant. How can I help you?")
        print("Good afternoon friend I am your virtual Assistant. How can I help you?")
    else:
        engine.say("Good evening friend I am your virtual Assistant. How can I help you?")
        print("Good evening friend I am your virtual Assistant. How can I help you?")

    engine.runAndWait()
    i=1
    while True:
        
        # speech recognizer
        

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        command=recognize_speech_from_mic(recognizer, microphone)
        if command['transcription'] is not None:
            command=command['transcription'].lower()
        else:
            continue
        print("your command is",command)
        # to know about Assistant
        if re.search('about yourself|your name|who are you',command):
            engine.say("hello my name is ubuntu Assistant")
            engine.runAndWait()

        if re.search('what can you do',command):
            print("I can send mail ,command me : send mail")
            print("I can search querry on google, command me : search or google")
            print("I can open browser ,command me:open browser or default browser or firefox")
            print("I can open terminal")
            print("I can open libreoffice draw,command me : open draw or wanna paint")
            print("I can open libreoffice calc,command me : open excel or open calc or spreadsheet")
            print("I can open libreoffice writer,command me : open writer")
            print("I can open terminal,command me : open terminal or terminal")
            print("I can shutdown pc,command me : shutdown")
            print("I can tell weather conditions,command me : weather or temperature")
            print("I can open youtube say me open youtube or search youtube")
            print("I can tell you today's day : command me : tell day")
            print("I can tell you current time : command me : tell me time or current time or what is the time")
            print("I can tell you todays date : command me : todays date or tell me date")
            print("I can open text editor,command me open text editor")
            print("I can shutdown your computer say me shutdown ")
            print("I can tell you about what I can do, command me :What can you do")
            print("I can tell you about my self, command me :about youself or your name or who are you")
            print("I can open visual studio command,command me: open visual studio code")
            print("If you want to exit you can command me: bye or exit")

        # to know date and time
        elif re.search("today's date|tell me date",command):
            current_date=get_date()
            print("current Date",current_date)
            engine.say("Todays date",current_date)
            engine.runAndWait()
        elif re.search('tell me time|current time|what is the time',command):
            current_time=get_time()
            print("current time",current_time)
            engine.say("Current time is :",current_time)
            engine.runAndWait()
            
        elif re.search('tell day',command):
            today=datetime.now().strftime("%A")
            print(today)
            engine.say("today is " +today)
            engine.runAndWait()
        elif re.search('weather|temperature',command):
            city=input("Enter city name")
            engine.say("Enter city name")
            engine.runAndWait()
            t,w=show_weather(city)
            print(t,w)
            engine.say("right now in "+str(city)+ "weather status is "+str(w)+"with temperature "+str(t))
            engine.runAndWait()
        elif re.search('shutdown|off',command):
            Choice=input("do you really want to shutdown your pc Y/N")
            if Choice=="Y":
                system_shutdown()
        elif re.search('open terminal|terminal',command):
            os.system("gnome-terminal")
        
        elif re.search('open browser|firefox|default browser',command):
            os.system("firefox")
        elif re.search('open texteditor',command):
            os.system('gedit')
        elif re.search('open writer',command):
            os.system('libreoffice --writer')
        elif re.search('open calc|open excel|spreadsheet',command):
            
            os.system('libreoffice --calc')
        elif re.search('open draw|wanna paint',command):
            os.system('libreoffice --draw')
        elif re.search('open visual studio |open code',command):
            os.system('code')
        elif re.search('send mail',command):
            try:
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login("senderpoonam@gmail.com","#1234567890")
                receiver_id=input("receiver id")
                message=input("message ?")
                s.sendmail("senderpoonam@gmail.com",receiver_id,message)
                print("message has been send")
                s.quit()
            except:
                print(" Sorry,some error occured!")
            
        elif re.search('google|search',command):
            print("google")
                
            search_google()
                
        elif re.search('open youtube|search youtube',command):
            engine.say("What can I search for you")
            engine.runAndWait()

            query=input("your query>>")
            
            webbrowser.open('https://www.youtube.com/results?search_query=%s' % query)
        elif re.search('wikipedia|wikipedia search',command):
            print("what you want to search")
            q=input("input your Query")
            r=wikipedia.summary(q,sentences=2)
            engine.say()
            engine.runAndWait()

        elif re.search('bye|exit',command):
            print(" You want to exit, Okay bye!")
            engine.say("You want to exit")
            engine.runAndWait()
            exit()
        else:
            print("No such command found")
            engine.say("No such command found")
            engine.runAndWait()

        
#Setup GUI
if __name__ == "__main__":
    Query()

