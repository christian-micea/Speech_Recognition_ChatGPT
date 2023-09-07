import speech_recognition as sr
import pyttsx3
import cv2

# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

try:
    print("Will stop on Ctrl+C press")
    # Loop infinitely for user to speak until escape is pressed
    while(1):   
        # Exception handling to handle
        # exceptions at the runtime
        try: 
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for 0.5 seconds to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, 0.2)

                #listens for the user's input
                audio2 = r.listen(source2)
        
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
    
                print("Said: ", MyText)
                SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occurred")

except KeyboardInterrupt:
    pass