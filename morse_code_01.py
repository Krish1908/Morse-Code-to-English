from playsound import playsound
import time

dict = { 'A':'.-', 'B':'-...',  'C':'-.-.', 'D':'-..', 'E':'.', 
        'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---',
        'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
        'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
        'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
        '1':'.----', '2':'..---', '3':'...--', 
        '4':'....-', '5':'.....', '6':'-....', 
        '7':'--...', '8':'---..', '9':'----.', 
        '0':'-----', " ":"/" } 


print("1. English to Morse Code")
print("2. Morse Code to English")
cases = input("Enter your option here: ")

if cases == '1':
    
    message = input('Enter your text message here: ')
    message = ' '.join(dict[c] for c in message.upper())
    print(message)

    # def play_sound(message):
    #     for c in message:
    #         if c == '.':
    #             playsound('short.mp3')
    #             time.sleep(0.1)
    #         elif c == '-':
    #             playsound('long.mp3')
    #             time.sleep(0.1)
    #         elif c == '/' or c == ' ':
    #             time.sleep(0.3)
    #         else :
    #             print("invalid")

    # play_sound(message)

elif cases == '2':
    message = input("Enter Morse Code here: ")
    reverse = {v : k for k,v in dict.items()}
    reverse_message = ''.join(reverse[c] for c in message.split(' '))
    print(reverse_message)