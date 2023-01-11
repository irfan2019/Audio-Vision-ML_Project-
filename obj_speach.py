from gtts import gTTS
from playsound import playsound
import sys

def text_to_speach(text=[]):
    final = ""
    # text = set(text)
    if not text:
        final = "There is no object detected"
    lang = "en"
    for t in text:
        if t in final:
            continue
        final += t
        if t == text[-1]:
            continue
        final += " and "
    output = gTTS(text=final, lang=lang, slow=False)
    output.save("new.mp3")
    #playsound("output.mp3")


if __name__ == "__main__":
    with open("coco.names") as f:
        data = f.read()
        data = data.split("\n")
    # text_to_speach(["person", "person"])
