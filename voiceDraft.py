import speech_recognition as sr
import recog_final as recog

# this is an draft of voice recognition code integrated with our software
# we were unable to do this because we needed wifi to download the required libs
def parseCommand():
    listener = sr.Recognizer()
    print('listening for a command')

    with sr.Microphone() as source: 
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        #print('listen beep bob')
        query = listener.recognize_google(input_speech,language = 'en_us')
        print(f'input speech was {query}')
    except Exception as exception:
        print('come again')
        #speak('come again')
        print(exception)
        return 'None'
    return query

file = open('inserted_code.py','w')
while True:
    query = parseCommand()
    file.write(recog_final(query))


