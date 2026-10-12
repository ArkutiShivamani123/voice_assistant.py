import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize TTS Engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)

            print("You Said:", command)

            return command.lower()

        except:
            return ""

def greet_user():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")

    elif hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your Python Voice Assistant.")

def execute_command(command):

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "open google" in command:

        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:

        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in command:

        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "weather" in command:

        speak("Opening weather information")
        webbrowser.open("https://www.google.com/search?q=current+weather")

    elif "search" in command:

        query = command.replace("search", "")

        speak(f"Searching for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    elif "wikipedia" in command:

        try:

            topic = command.replace("wikipedia", "")

            result = wikipedia.summary(
                topic,
                sentences=2
            )

            speak(result)

        except:

            speak("Sorry, I could not find that topic.")

    elif "exit" in command:

        speak("Goodbye")
        return False

    else:

        speak(
            "I did not understand. Please repeat."
        )

    return True

# MAIN PROGRAM

greet_user()

running = True

while running:

    command = take_command()

    if command:

        running = execute_command(command)
        