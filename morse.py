'''Conversor de Morse a Ascii y de Ascii a Morse.
   Creado por Pau Rosselló(prossellob) el 17/8/2017
   
   Introduce el mensaje que quieras convertir y listo.
'''

alphabet = {   "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    " " : "/",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "," : ",",
    "!" : "!",
    "?" : "?"}
morsealphabet = {}
for k, v in alphabet.items(): #Convierte los valores en llaves del dicc.
    morsealphabet[v] = k


def morse_char(code):
    code,message = code.split(' '),''
    for item in code:
        message += morsealphabet[item]
    print(message)

def char_morse(code):
    message = ''
    for char in code:
        message += (alphabet[char] + ' ')
    print(message)

print('¡Cuidado! NO DEJES ESPACIOS AL FINAL O AL PRINCIPIO.')
string_a_convertir = str(input('Ingrese el mensaje: '))

#Revisa si es morse o caracateres alfanumericos.
if string_a_convertir[0] == '.' or string_a_convertir[0] == '-':
    morse_char(string_a_convertir)
elif string_a_convertir[0].isalpha():
    char_morse(string_a_convertir.lower())
else:
    if string_a_convertir[1] == '.' or string_a_convertir[0] == '-':
        morse_char(string_a_convertir)
    elif string_a_convertir[1].isalpha():
        char_morse(string_a_convertir.lower())
