from math import ceil
from collections import Counter

isCode = ""

dictionaryFile = open("../dictionary.txt")
dictionary = Counter()
words = dictionaryFile.read().split("\n")
dictionary.update(words)

while isCode != "C" and isCode != "D" and isCode != "B":
    isCode = input("Do u want to (C)ode , (D)ecode with code or (B)rute force your message: ")
    isCode = isCode.upper()

message = input("Insert your mesasge: ")

if isCode == "C":
    code = ""
    while not code.isdigit():
        code = input("Insert your code(1 to inf): ")

    code = int(code)
    answer = ""

    for i in range(0, code):
        for j in range(i, len(message), code):
            answer += message[j]
    
    print(answer)

elif isCode == "D":
    code = ""
    while not code.isdigit():
        code = input("Insert your code(1 to inf): ")

    c = int(code)
    code = ceil(len(message)/int(code))
    answer = ""
    if len(message) < code * c:
        dif = code * c - len(message)

        for i in range(dif):
            message = message[:len(message)-code*i] + " " + message[len(message)-code*i:]

    for i in range(0, code):
        for j in range(i, len(message), code):
            answer += message[j]

    print(answer)

elif isCode == "B":

    # Proof that it works :))
    # message = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    variants = []

    for c in range(1, len(message)):
        code = ceil(len(message)/c)
        variant = ""
        newMes = message
        if len(newMes) < code * c:
            dif = code * c - len(newMes)
            
            for i in range(dif):
                newMes = newMes[:len(newMes)-code*i] + " " + newMes[len(newMes)-code*i:]

        for i in range(0, code):
            for j in range(i, len(newMes), code):
                variant += newMes[j]

        variants.append(variant)
    
    for variant in variants:
        k = 0
        for word in variant.split(" "):
            if word.upper() in dictionary:
                k += 1
            if k == 3:
                print(variant)
                break