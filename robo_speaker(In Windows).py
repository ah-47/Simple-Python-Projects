import os
import pyttsx3

if __name__ == '__main__':
    print('Welcome to Robo Speaker')
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:
        x = input('What do you want me to speak (enter "q" to exit): ')
        if x == 'q':
            engine.say('Goodbye!')
            engine.runAndWait()
            break

        # Speak the input text
        engine.say(x)
        engine.runAndWait()
