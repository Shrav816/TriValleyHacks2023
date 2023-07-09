import speech_recognition as sr 
import pytts3x

# speech engine
engine = pytts3x.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voice[1].id)
activationWord= 'computer'

def speak(text):
    rate = 180
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

    def parseCommand():
    listener = sr.Recognizer()
    print('listening for a command')

    with sr.Microphone() as source: 
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        print('listen beep bob')
        query = listener.recognize_google(input_speech,language = 'en_us')
        print(f'input speech was {query}')
    except Exception as exception:
        print('come again')
        speak('come again')
        print(exception)
        return 'None'
    return query


if __name__ == '__main__':
    speak('activation complete')

    while True:
        #parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

        