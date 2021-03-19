# importing the Google Text To Speech Lib
from gtts import gTTS
#importing os module in Python
import os
# add the text that is requird to be converted into audio 
mytext = ''
#chose the language that you want the audio in
language = 'en'
# Passing the text and language to gTTS lib
#Slow=False is that which tells the lib to increse the speed of the audio
myobj = gTTS(text=mytext, lang=language, slow=False)
#Saves the audio file in the (C:\Users\) directory mostly
myobj.save("audio.mp3")
#automatically runs the audio.mp3 file
os.system("audio.mp3")
