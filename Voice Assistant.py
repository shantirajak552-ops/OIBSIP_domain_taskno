import datetime
import webbrowser

print("🤖 Voice Assistant Started!")
print("Type 'hello', 'time', 'date', 'search', or 'bye'")

while True:
    command = input("\nYou: ").lower()

    if command == "hello":
        print("Assistant: Hello! How can I help you?")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Assistant: The current time is", current_time)

    elif command == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Assistant: Today's date is", current_date)

    elif command.startswith("search "):
        query = command[7:]
        print("Assistant: Searching for", query)
        webbrowser.open("https://www.google.com/search?q=" + query)

    elif command == "bye":
        print("Assistant: Goodbye! 👋")
        break

    else:
        print("Assistant: Sorry, I don't understand that command.")