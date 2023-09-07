import speech_recognition as sr
import pyttsx3
import os
import openai

openai.api_key_path = "C:\Work\Chris\Programare vara cu Razvan\Audio ChatGPT\OpenAI_Key.txt"

# Initialize the recognizer
r = sr.Recognizer()
 
# Function to convert text to
# speech
def speakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def recordText():
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
    
            print("user: ", MyText)
    
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")

    return MyText

def sendToChatGPT(message, currModel = "gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model = currModel,
        messages = message,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    
    output = response.choices[0].message.content
    message.append(response.choices[0].message)
    return output

message = []
try:
    while(True):
        text = recordText()
        message.append({"role": "user","content": text})
        response = sendToChatGPT(message)
        print("chatGPT: ", response)
        speakText(response)
except KeyboardInterrupt:
    pass