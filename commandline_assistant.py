import datetime
import webbrowser
import sys

def greet():
    print("Hello! I am your Python assistant.")
    print("You can type commands like:\n - time\n - date\n - search for <something>\n - exit")

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    today = datetime.datetime.now()
    return today.strftime("%B %d, %Y")

def assistant():
    greet()
    while True:
        command = input("\n> ").lower()

        if "hello" in command:
            print("Assistant: Hello there!")

        elif "time" in command:
            print("Assistant: The time is", get_time())

        elif "date" in command:
            print("Assistant: Today's date is", get_date())

        elif "search for" in command:
            query = command.replace("search for", "").strip()
            url = "https://www.google.com/search?q=" + query.replace(" ", "+")
            print("Assistant: Searching for", query)
            webbrowser.open(url)

        elif "exit" in command or "quit" in command:
            print("Assistant: Goodbye!")
            sys.exit()

        else:
            print("Assistant: I don't understand that.")

assistant()
