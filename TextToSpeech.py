from gtts import gTTS
import os
with open(r"C:\\Users\haru8\github\watson-streaming-stt\audio.txt","r")as file:
    textFile = file.read()
language = "en"
myobj = gTTS(text=textFile, lang=language, slow=False)
myobj.save("tts.mp3")
os.system("start tts.mp3")
