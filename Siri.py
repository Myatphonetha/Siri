# import openai
# import pyttsx3
# import speech_recognition as sr
# import time 

# openai.api_key = ""


# #Initialize the text to speech 
# engine = pyttsx3.init()


# def audio_to_text(filenames): #audio files
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(filenames) as source:
#         audio = recognizer.record(source)
#     try:
#         return recognizer.recognize_google(audio)
#     except:
#         print ("Unknown error")

# def generate_speech(prompt): #speech
#     response = openai.Completion.create(
#         engine = "text-davinci-003",
#         prompt = prompt,
#         max_tokens = 4000, 
#         n = 1, 
#         stop = None, 
#         temperature = 0.5,
#     )
#     return response["choices"][0]["text"]

# def speak_text(text): #speech
#     engine.say(text)
#     engine.runAndWait()

# def main(): #
#     while True:
#         print ("Say Siri to wake her up")
#         with sr.Microphone() as source:
#             recognizer = sr.Recognizer()
#             audio = recognizer.listen(source)
#             try:
#                 transcription = recognizer.recognize.google(audio)
#                 if transcription.lower() == "Siri":
#                     #recordAutio
#                     filename = "input.wav"
#                     with sr.Microphone() as source:
#                         recognizer = sr.Recognizer()
#                         source.pause_threshold = 1
#                         audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
#                         with open (filename, "wb")as f:
#                             f.write(audio.get_wav_data())
                    
#                     #transcribe audio to txt 
#                     text = audio_to_text(filename)
#                     if text:
#                         print (f"You said: %s" % text)

#                         #Generate response using GPT
#                         print (f"Siri: %s" % {response})

#                         speak_text = (response)
#             except Exception as e:
#                 print("An error occurred:{}".format(e))


# if __name__ == "__main__":
#     main()

import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"  # Add your OpenAI API key here

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def generate_speech(prompt, voice='default'):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output_text = response.choices[0].text
    if voice == 'siri':
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    else:
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.default')
    return output_text

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    # Initial interaction to simulate Siri
    initial_prompt = "Hi, I'm Siri. How can I help you today?"
    initial_response = generate_speech(initial_prompt, voice='siri')
    print(f"Siri: {initial_response}")
    speak_text(initial_response)

    while True:
        print("Say 'Siri' to wake her up")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "siri":
                    # Record Audio
                    filename = "input.wav"
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe audio to text
                    text = audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                        # Generate response using GPT
                        response = generate_speech(text, voice='siri')
                        print(f"Siri: {response}")

                        speak_text(response)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
