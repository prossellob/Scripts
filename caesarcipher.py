inp1 = input('Input the text you want to code:\n')
inp1 = inp1.lower()

key = int(input('Input the key you want to use from 1 to 25:\n'))

def caeserchiper(input,key): #Function to code a text with caeser chyper.
    if key > 25:
        key = 25
    elif key < 1:
        key = 1
    finaltext = ''
    for letter in input:
        if letter.isalpha():
            num = ord(letter)
            if (num + key) > 122:
                x = (num + key) - 122
                finaltext += chr(x + ord('a') - 1)
            elif((num + key <= 122)):
                finaltext += chr(num + key)
        else:
            finaltext += letter
    print(finaltext)

caeserchiper(inp1,key)
