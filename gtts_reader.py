import uuid, os
from gtts import gTTS
from playsound import playsound

class Reader:
    def __init__(self, options):
        self.myid = ""
        if options == {}:
            self.options = {"lang": "en"}
        else:
            self.options = options

    def read(self, data):
        tts = gTTS(text=data, lang=self.options["lang"])
        self.myid = str(uuid.uuid4()) + ".mp3"
        tts.save(self.myid)
        playsound(self.myid)
        os.remove(self.myid)

    def exceptions_handle(self):
        try:
            os.remove(self.myid)
        except FileNotFoundError:
            pass