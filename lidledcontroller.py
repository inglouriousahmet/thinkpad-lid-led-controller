import time
import os


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def text_to_morse(text):
    mors_message = ""
    for letter in text.upper():
        mors_message += MORSE_CODE_DICT[letter] + " "
    
    return mors_message
        
        
def led(state):        
    if state:
        os.system("echo 1 > /sys/class/leds/tpacpi\:\:lid_logo_dot/brightness")
    else:
        os.system("echo 0 > /sys/class/leds/tpacpi\:\:lid_logo_dot/brightness")
        
    
    
def run():
    message = "naber"
    morse_code_message = text_to_morse(text=message)
    
    led(False)
    
    for letter_index in range(len(morse_code_message)):
        print(morse_code_message[letter_index])
              
        if(morse_code_message[letter_index] == "-"):
            led(True)
            time.sleep(0.50)
            led(False)
            time.sleep(1)
            
        elif(morse_code_message[letter_index] == "."):
            led(True)
            time.sleep(0.15)
            led(False)
            time.sleep(1)
            
        elif(morse_code_message[letter_index] == " "):
            led(False)
            time.sleep(1)


run()