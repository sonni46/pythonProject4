from gtts import gTTS
import os


print()
text = input("Scrivi quello che vuoi far dire al programma: ")
language = input('Scegli lingua: ')

output = gTTS(text=text,lang=language,slow=False)

output.save("txtSpeech.mp3")

os.system("start txtSpeech.mp3")