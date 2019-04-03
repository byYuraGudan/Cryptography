#-*-coding: utf8 -*-
import cezarCrypto,re

DIC = {'a': '0', 'b': '1',
 'c': '2', 'd': '3',
 'e': '4', 'f': '5',
 'g': '6', 'h': '7',
 'i': '8', 'j': '9',
 'k': '10', 'l': '11',
 'm': '12', 'n': '13',
 'o': '14', 'p': '15',
 'q': '16', 'r': '17',
 's': '18', 't': '19',
 'u': '20', 'v': '21',
 'w': '22', 'x': '23',
 'y': '24', 'z': '25',
 ' ': '26'}

def ask(quest, cond=None):
    """Enter with keyboard"""
    while True:
        if cond == 'd':
            answer = input(quest)
            if not answer.isdigit():
                print('Only digits')
                continue
            else:
                return int(answer)
        answer = input(quest)
        if re.search(r'[^a-zA-Z \',.:"?!]', answer):
            print('Only English alph')
            continue
        return answer.lower()



def replaceEncode(string,key):
    string = string.lower()
    string = cezarCrypto.cEncode(string, key)
    tmp = list(string)
    stroka = ""
    for symbol in tmp:
        if get_items(DIC,symbol)is not None:
            stroka += " %s"%str(get_key(DIC,symbol))
    return stroka[1:]


def replaceDecode(string,key):
    tmp = string.split(" ")
    stroka = ""
    for symbol in tmp:
        if get_items(DIC,symbol)is not None:
            stroka += "%s"%str(get_items(DIC,symbol))
    stroka = cezarCrypto.cDecode(stroka, key)
    return stroka

def get_key(dic, val):
    for i in dic.items():
        if val in i:
            return i[1]

def get_items(dic,val):
    for i in dic.items():
        if val in i:
            return i[0]

def openFile(file):
    f = open(file,mode = 'r')
    print('open file - %s'%file)
    return f.read()

def saveFile(string,fileOut):
    f2 = open(fileOut, mode ='w+')
    f2.write(string)
    f2.close()
    print('save file - %s'%fileOut)

def main():
    while True:
        string = ask('Enter file name: ')
        enDe = ask('Encode or Decode(e/d): ')
        key = ask('Enter the key: ', 'd')
        if enDe == 'e' or enDe == 'encode':
            enc = replaceEncode(openFile(string),key)
            print(enc)
            saveFile(enc,'fileEncode.txt')
        elif enDe == 'd' or enDe == 'decode':
            dec = replaceDecode(openFile(string),key)
            print(dec)
            saveFile(dec,'fileDecode.txt')
        else:
            continue

if __name__ == '__main__':
    main()