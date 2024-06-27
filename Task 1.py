import speech_recognition as sr
import pyttsx3
import wikipedia
import wolframalpha
import webbrowser
import datetime
import requests

# Initialize the text-to-speech engine
engine = pyttsx3.init()

"""Convert text to speech."""
def speak(text):
	engine.say(text)
	engine.runAndWait()

"""Listen to the user's command and convert it to text."""
def listen():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		audio = recognizer.listen(source)
		try:
			print("Recognizing...")
			query = recognizer.recognize_google(audio, language='en-US')
			print(f"User said: {query}")
		except sr.UnknownValueError:
			print("Sorry, I didn't catch that. Could you please repeat?")
			return "None"
		except sr.RequestError:
			print("Could not request results; check your network connection.")
			return "None"
		return query.lower()

"""Search Wikipedia for the given query."""
def search_wikipedia(query):
	try:
		results = wikipedia.summary(query, sentences=2)
		speak("According to Wikipedia")
		print(results)
		speak(results)
	except wikipedia.exceptions.DisambiguationError as e:
		speak("The term is ambiguous, please be more specific.")
	except wikipedia.exceptions.PageError:
		speak("No page found for the given term.")
	except Exception as e:
		speak("Sorry, I couldn't find any information on that.")

"""Open the specified URL in the web browser."""
def open_website(url):
	webbrowser.open(url)

"""Get the current time and speak it."""
def get_time():
	now = datetime.datetime.now().strftime("%H:%M:%S")
	speak(f"The time is {now}")

"""Main function to run the voice assistant."""
def main():
	speak("Hello! How can I assist you today?")
	while True:
		query = listen()
		if 'wikipedia' in query:
			speak("Searching Wikipedia...")
			query = query.replace("wikipedia", "")
			search_wikipedia(query)
		elif 'open youtube' in query:
			speak("Opening YouTube")
			open_website("https://www.youtube.com")
		elif 'time' in query:
			get_time()
		elif 'exit' in query or 'bye' in query:
			speak("Goodbye!")
			break
		else:
			speak("I am not sure how to help with that.")

if __name__ == "__main__":
	main()