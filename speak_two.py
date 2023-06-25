import speech_recognition as sr

# Crea un objeto de reconocimiento de voz
r = sr.Recognizer()

while True:
    # Utiliza el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("say something...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language='es')

        # print text
        print(texto)

    except sr.UnknownValueError:
        print("Can not understand the audio")

    except sr.RequestError as e:
        print("Error requesting the results of the speech recognition service: {0}".format(e))