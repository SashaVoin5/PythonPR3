import threading
from RandomWordGenerator import RandomWord
import os
from random import randint
from typing import List

def create (thread_num):
    r = randint(100000, 5000000)
    Random = RandomWord()
    Random.constant_word_size = False
    tread=str(thread_num)
    name=str(os.getpid())
    file = open("C:/test/files/"+"thread-"+tread+"-"+ name+".txt", "a")
    for w in range(r):
        file.write(f'{Random.generate()}\n')
    file.close()
    print(f"File numb{thread_num} is create")
    path="C:/test/files/"+"thread-"+tread+"-"+ name+".txt"
    check(path)




list_tread : List[threading.Thread] = []
for i in range(8):
    thread = threading.Thread(target=create, args=(i,)) #Надо было работать с процессом, а не с потоком.Но почему-то при работе с процессом даже не запускается скрипт.
    thread.start()
    list_tread.append(thread)
[thread.join() for thread in list_tread]


def length(named):
    file = open(named, 'r')
    k = 0
    for line in file:
        k += 1
    file.close()
    return k

def total(named: str):
    file = open(named, 'r')
    t = 0
    for line in file:
        for word in line:
            if word != '\n':
                t += len(word)
    file.close()
    return t

def maxlength(named: str):
    file = open(named, 'r')
    maxlenth: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if maxlenth == -1:
                maxlenth = len(line)
            else:
                if maxlenth < len(line):
                    maxlenth = len(line)
    file.close()
    return maxlenth

def minlength(named: str):
    file = open(named, 'r')
    minlenth: int = -1
    for line in file:
        line = line.replace("\n", "")
        if line != '':
            if minlenth == -1:
                minlenth = len(line)
            else:
                if minlenth > len(line):
                    minlenth = len(line)
    file.close()
    return minlenth

def middlelength(named: str):
    middlelenth: int = total(named) / length(named)
    return middlelenth

def consonant(named: str):
    file = open(named, 'r')
    consonant: int = 0
    for line in file:
        for p in line:
            if p in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y', '\n', ' ']:
                pass
            else:
                consonant += 1
    file.close()
    return consonant

def vowel(named: str):
    file = open(named, 'r')
    vow: int = 0
    for line in file:
        for p in line:
            if p in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
                vow += 1
            else:
                pass
    file.close()
    return vow

def repetitions(named: str):
    file = open(named, 'r')
    list_file: List[str] = file.read().split()
    diction: dict = dict()

    for word in list_file:
        if len(word) in diction:
            diction[len(word)] += 1
        else:
            diction[len(word)] = 1

    sorted_dict = {}
    sorted_keys = sorted(diction.keys())

    for w in sorted_keys:
        sorted_dict[w] = diction[w]
    rep_dict = sorted_dict.copy()

    rep: str = ""
    for key in diction:
        rep += f"   * {key} simv. >> {diction[key]} repeat.\n"
    file.close()
    return rep

def check(path):
    print(f"********************************************************\n"
          f"  Analize for file {file}\n"
          f"********************************************************\n"
          f"1. All sim --> {total(path)}\n" +
          f"2. Max len word --> {maxlength(path)}\n" +
          f"3. Min len word --> {minlength(path)}\n" +
          f"4. Avg lin word --> {middlelength(path)}\n" +
          f"5. number of vowels --> {vowel(path)}\n" +
          f"6. number of consonant --> {consonant(path)}\n" +
          "7. Number of repetitions of words with the same length:\n" +
          f"{repetitions(path)} \n")
