import speech_recognition as sr

def recognize_voice():
    print('Starting...')
    # Create a voice recognition object
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)

        try:
            # Use Google's speech recognition to convert audio into text
            text = r.recognize_google(audio, language='en')

            # Print the recognized text
            print(text)

            # Check if the word "stop" was said
            if "stop" in text.lower():
                print("Stopping voice recognition...")
                break  # Exit the while loop to stop the recognition

        except sr.UnknownValueError:
            print("Could not understand the audio")

        except sr.RequestError as e:
            print("Error requesting the results of the speech recognition service: {0}".format(e))

recognize_voice()
