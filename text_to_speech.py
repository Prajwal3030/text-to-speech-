from gtts import gTTS
import os

fh = open("test.txt","r")

myText =fh.read().replace("\n"," ")

language = 'en'
output = gTTS(text=myText, lang=language, slow=False)


output_path = os.path.join(os.getcwd(), "output.mp3")

fh.close()

try:
    output.save(output_path)
    print("Audio file saved successfully.")
except Exception as e:
    print(f"Error saving audio file: {e}")

try:
    os.system(f"Invoke-Item '{output_path}'")
    print("Audio file playback initiated.")
except Exception as e:
    print(f"Error playing audio file: {e}")

