import speech_recognition as speechrecognizer
from playsound import playsound

class SpeechRecognition:
    def __init__(self):
        self.recognizer = speechrecognizer.Recognizer()
    
    def play_ding_sound(self, sound_file):
        playsound(sound_file)

    def record_audio(self):
        with speechrecognizer.Microphone() as source:
            self.play_ding_sound("notification-sound-7062.wav") 
            audio = self.recognizer.listen(source)
            self.play_ding_sound("notification-sound-7062.wav") 
            return audio

    def transcribe_audio(self, audio):
        try:
            transcription = self.recognizer.recognize_google(audio)
            return transcription
        except speechrecognizer.UnknownValueError:
            return "Could not understand audio"
        except speechrecognizer.RequestError:
            return "Could not request results; check your network connection"
        

speech_recognition = SpeechRecognition()
audio_data = speech_recognition.record_audio()
transcription = speech_recognition.transcribe_audio(audio_data)
print(transcription)