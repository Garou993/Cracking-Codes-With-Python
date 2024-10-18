from sys import exit
from collections import Counter

isCode = ""

dictionaryFile = open("../dictionary.txt")
dictionary = Counter()
words = dictionaryFile.read().split("\n")
dictionary.update(words)

while isCode != "C" and isCode != "D" and isCode != "B":
    isCode = input("Do u want to (C)ode, (D)ecode or (B)rute force your message: ")
    isCode = isCode.upper()

message = input("Insert your mesasge: ")
message = message.upper()

def transformLetter(letter, code1, code2): 
    asciiLetter = ord(letter)

    if asciiLetter < 65 or asciiLetter > 90:
        return letter
    
    asciiLetter -= 65
    asciiLetter = asciiLetter * code1 + code2
    if asciiLetter > 25:
        asciiLetter %= 26

    return chr(asciiLetter + 65)

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m 

def reverseLetter(letter, code1, code2): 
    asciiLetter = ord(letter)

    if asciiLetter < 65 or asciiLetter > 90:
        return letter
    
    asciiLetter -= 65
    asciiLetter = asciiLetter - code2
    if asciiLetter < 0:
        asciiLetter = 26 + asciiLetter
    asciiLetter = asciiLetter * findModInverse(code1, 26) % 26

    return chr(asciiLetter + 65)

def checkCodes(code1, code2):
    if code1 <= 1:
        exit("Cypher is weak when code 1 is 1. Chose a different code")
    elif code2 <= 0:
        exit("Cypher is weak when code 2 is 0. Chose a different code")
    elif gcd(code1, 26) != 1:
        exit("Code 1 and alphabet length are not realtively prime. Chose a different code")

if isCode == "C":
    code1 = ""
    while not code1.isdigit():
        code1 = input("Insert your code 1(1 to inf): ")
    code1 = int(code1)

    code2 = ""
    while not code2.isdigit():
        code2 = input("Insert your code 2(1 to inf): ")
    code2 = int(code2)
    if code2 > 25:
        code2 %= 26

    checkCodes(code1, code2)

    answer = ""
    for letter in message:
        answer += transformLetter(letter, code1, code2)
    
    print(answer)

if isCode == "D":
    code1 = ""
    while not code1.isdigit():
        code1 = input("Insert your code 1(1 to inf): ")
    code1 = int(code1)

    code2 = ""
    while not code2.isdigit():
        code2 = input("Insert your code 2(1 to inf): ")
    code2 = int(code2)
    if code2 > 25:
        code2 %= 26

    checkCodes(code1, code2)

    answer = ""
    for letter in message:
        answer += reverseLetter(letter, code1, code2)
    
    print(answer)

if isCode == "B":
    # Proof that it works    
    # message = """"UVKKJ! BX SFBV LZ CFBVZ FSE L FB QUV WVZQ NJEVI VYVI!!!"""

    for code1 in range(2, 26**2):

        if gcd(code1, 26) != 1:
            continue
        
        for code2 in range(1, 26):
            answer = ""
            for letter in message:
                answer += reverseLetter(letter, code1, code2)
            
            k = 0
            for word in answer.split(" "):
                if word.upper() in dictionary:
                    k += 1
                if k == 3:
                    print(answer, code1, code2)
                    break