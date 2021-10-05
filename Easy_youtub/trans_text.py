
#음성변환

import speech_recognition as sr

r =  sr.Recognizer()

with sr.Microphone() as source:

    print('Speak Anything : ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='ko-KR')
        print('You said : {}'.format(text))
    except:
        print('목소리를 인식하지 못했습니다')