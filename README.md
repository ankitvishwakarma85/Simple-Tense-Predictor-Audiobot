# Simple_Tense_Predictor_Audiobot
 A simple tense predictor trained using Textblob's NaiveBayesClassifier that takes audio input and plays an audio stating the tense of the sentence.

## Installations:
 1) *TextBlob* -> To import the NaiveBayesClassifier 
 2) *speech_recognition* -> To listen to audio directly from the microphone and convert to text
 3) *gtts* -> To convert text to audio
 4) *playsound* -> To play the audio output
 5) *pickel* -> To store trained model for reusing it again , Note: pickel is already a part of python's downloaded library
 
 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install any of the above modules.

 ```bash
 pip install module_name
 ```

## Explaination:

**Train.py**

1) Made the necessary imports (textblob,pickle).
2) Passed a list of tuples of the form ('sentence','label') named training (train set) to the NBC function with returns a trained model.
3) Created a list of tuples of the form ('sentence','label') named test (test set) to check the models accuracy again this examples.
4) Predicted tense of some example sentences.
5) Stored the model inside a file named model.pickle.

**Test.py**

1) Made the necessary imports (textblob,pickle,gtts,speech_recognition,playsound).
2) Loaded the model from the model.pickel file created earlier.
3) speech_recognition module is used to connect to the microphone and take an audio input.
4) speech_recognition's adjust_for_ambient_noise() method adapts to the noise in the background the other speech_recognition are pretty self explanatory.
5) The model is used to predict the tense of the text extracted from the audio input.
6) The output value of the tense along with the input statement is that concatinated and converted to an audio file using the gtts module.
7) playsound is used to play that audio file aloud.
8) In case an exception is raised the program asks for the audio input again.

For any queries/suggestions contact on *ankitvishwakarma85@gmail.com*
