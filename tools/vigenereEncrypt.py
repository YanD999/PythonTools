# get user input via terminal
choice = input("Do you want to E(ncrypt) or D(ecrypt)? ")
message = input("Type the message in: ")
key = input("Type the key you want to use: ")

letterslist = {'a': 0,  'A': 1, 'b': 2,  'B': 3, 'c': 4,  'C': 5, 'd': 6,  'D': 7, 'e': 8,  'E': 9, 'f': 10,  'F': 11,
               'g': 12,  'G': 13, 'h': 14,  'H': 15, 'i': 16,  'I': 17, 'j': 18,  'J': 19, 'k': 20, 'K': 21, 'l': 22,
               'L': 23, 'm': 24, 'M': 25, 'n': 26, 'N': 27, 'o': 28, 'O': 29, 'p': 30, 'P': 31, 'q': 32, 'Q': 33, 'r': 34,
               'R': 35, 's': 36, 'S': 37, 't': 38, 'T': 39, 'u': 40, 'U': 41, 'v': 42, 'V': 43, 'w': 44, 'W': 45, 'x': 46,
               'X': 47, 'y': 48, 'Y': 49, 'z': 50, 'Z': 51, 'à': 52, 'â': 53, 'ä': 54, 'å': 55, 'ã': 56, 'À': 57, 'Â': 58,
               'Ä': 59, 'Å': 60, 'é': 61, 'è': 62, 'ê': 63, 'ë': 64, 'É': 65, 'È': 66, 'Ê': 67, 'Ë': 68, 'í': 69, 'ì': 70,
               'î': 71, 'ï': 72, 'Í': 73, 'Ì': 74, 'Î': 75, 'Ï': 76, 'ô': 77, 'ö': 78, 'õ': 79, 'Ô': 80, 'Ö': 81, 'Õ': 82,
               'ù': 83, 'û': 84, 'ü': 85, 'Ù': 86, 'Û': 87, 'Ü': 88, 'ç': 89, 'Ç': 90, 'ý': 91, 'ÿ': 92, 'Ý': 93, 'Ÿ': 94,
               '×': 95, 'Ø': 96, 'Þ': 97, 'ð': 98, '(': 99, ')': 100, '"': 101, "'": 102, '?': 103, ',': 104, '!': 105,
               ':': 106, ';': 107, '.': 108, '/': 109, '*': 110, '-': 111, '+': 112, '<': 113, '>': 114, '&': 115, '#': 116,
               '~': 117, '€': 118, '$': 119, '|': 120, '§': 121, '%': 122, '0': 123, '1': 124, '2': 125, '3': 126, '4': 127,
               '5': 128, '6': 129, '7': 130, '8': 131, '9': 132, '=': 133, '@': 134, '[': 135, ']': 136, '{': 137, '}': 138,
               '°': 139, 'æ': 140, 'Æ': 141, 'œ': 142, '¢': 143, '£': 144, '¥': 145, 'ƒ': 146, 'ñ': 147, 'Ñ': 148, '¿': 149,
               '¬': 150, '½': 151, '¼': 152, '«': 153, '»': 154, '¦': 155, 'ß': 156, 'µ': 157, '±': 158, '¾': 159, '·': 160,
               '²': 161, '…': 162, '†': 163, '‡': 164, '^': 165, '‰': 166, 'Š': 167, '`': 168, '´': 169, '“': 170, '”': 171,
               '–': 172, '_': 173, '™': 174, 'š': 175, '¨': 176, '©': 177, '®': 178, ' ': 179, '³': 180, '¹': 181, '•': 182, '*/avoid\'breaking' : 183}
# when adding a character -> update(+1) int (181) in encrypt and decrypt

def wordToIntArray(word): # returns an array with for each letter the corresponding integer
    array = []
    for letter in word:
        array.append(letterslist[letter])
    return array

def encrypt(): # returns an array with the integer value of each letter of the message + the key
    wordArray = wordToIntArray(message)
    keyArray = wordToIntArray(key)
    wordAndKeyArray = []
    index = 0
    for w in wordArray:
        if index == len(keyArray):
            index = 0
        intvalue = w + keyArray[index]
        if intvalue > 184: # when number greater than list size
            intvalue -= 183
        wordAndKeyArray.append(intvalue)
        index +=1
    return wordAndKeyArray

def decrypt(): # returns an array with the integer value of each letter of the message - the key
    wordAndKeyArray = wordToIntArray(message)
    keyArray = wordToIntArray(key)
    wordArray = []
    index = 0
    for w in wordAndKeyArray:
        if index == len(keyArray):
            index = 0
        intvalue = w - keyArray[index]
        if intvalue < 0: # when number smaller than list
            intvalue += 183
        wordArray.append(intvalue)
        index += 1
    return wordArray

def intToWord(messageArray): # takes int[] and returns a string
    out = ""
    for s in messageArray:
        out += list(letterslist.keys())[list(letterslist.values()).index(s)]
    return out

def execute():
    if message == '' or key == '': # no message or key given
        print("You forgot to fill in something. Please try again")
        exit()
        
    if choice == 'd' or choice == 'D' or choice == 'decrypt' or choice == 'Decrypt':
        mess = decrypt()
    else: # default
        mess = encrypt()
    print(intToWord(mess))
    return intToWord(mess)

execute()