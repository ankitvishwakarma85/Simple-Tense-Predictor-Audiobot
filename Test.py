from textblob.classifiers import NaiveBayesClassifier as NBC #https://en.wikipedia.org/wiki/Naive_Bayes_classifier
from textblob import TextBlob
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import pickle

with open(r"model.pickle", "rb") as input_file:
    model = pickle.load(input_file)

r = sr.Recognizer()

while(1):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration = 0.2)
        print("Listening... ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Output:",text)
            Value = model.classify(text)
            print(Value)
            text = text[:] + ' is a ' + Value + "Tense Sentence."
            language = "en" # for english
            speech = gTTS(text = text,tld="com",lang = language ,slow=False)
            speech.save("Output.mp3")
            playsound("Output.mp3")
            break
        except:
            print("I did not get that\nTrying Again: ")
'''
print(model.classify("Patrick is going to the library."))
print(model.classify("Albert was sick."))
print(model.classify("Dona will prepare the dessert."))
'''