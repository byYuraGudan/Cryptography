#-*-coding: utf8 -*-

import re

DIC = {chr(x): x-97 for x in range(97, 123)}


def ask(quest, cond=None):
    '''прием ввода с клавиатуры'''
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


def cEncode(string, key):
    new_string = ''
    for i in string:
        if i not in DIC:
            new_string += i
            continue
        ch = DIC[i] + key
        if ch > 25:
            ch = ch - 26
        new_string += get_key(DIC, ch)
    return new_string


def cDecode(string, key):
    new_string = ''
    for i in string:
        if i not in DIC:
            new_string += i
            continue
        ch = DIC[i] - key
        if ch < 0:
            ch = 26 + ch
        new_string += get_key(DIC, ch)
    return new_string


def get_key(dic, val):
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
            enc = cEncode(openFile(string),key)
            print(enc)
            saveFile(enc,'fileEncode.txt')
        elif enDe == 'd' or enDe == 'decode':
            dec = cDecode(openFile(string),key)
            print(dec)
            saveFile(dec,'fileDecode.txt')
        else:
            continue

if __name__ == '__main__':
    main()
