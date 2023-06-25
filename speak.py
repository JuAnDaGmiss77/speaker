import speech_recognition as sr

def recognize_voice():
    print('comming')
    # object
    r = sr.Recognizer()

    while True:
        # Utiliza el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("say something...")
            audio = r.listen(source)

        try:
            # Use speech recognition to convert audio to text
            texto = r.recognize_google(audio, language='es')

            # Print the recognized text
            print(texto)

        except sr.UnknownValueError:
            print("Can not understand the audio")

        except sr.RequestError as e:
            print("Error requesting the results of the speech recognition service; {0}".format(e))

recognize_voice()
