import keyboard
import datetime
import webbrowser

def greet():
    responses = ["Hello!", "Hi there!", "Greetings!"]
    return responses

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}"

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def voice_assistant():
    print("Say something...")

    try:
        while True:
            if keyboard.is_pressed("enter"):
                command = input("You said: ").lower()

                if "hello" in command:
                    response = greet()
                elif "time" in command:
                    response = get_time()
                elif "search" in command:
                    query = command.split("search")[-1].strip()
                    response = f"Searching the web for {query}"
                    search_web(query)
                else:
                    response = "I didn't understand that."

                print("Assistant:", response)

    except KeyboardInterrupt:
        print("Voice assistant terminated.")

if __name__ == "__main__":
    voice_assistant()
