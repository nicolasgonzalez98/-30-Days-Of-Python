import re

def count_lines_and_words(file):
    regExp = r'\W'
    path = '../../data/'+file
    with open(path) as f:
        lines = f.readlines()
        number_lines = 0
        number_words=0
        for l in lines:
            if l != '\n':
                palabras = l.split()
                for w in palabras:
                    if w != '-':
                        number_words+=1
                
                number_lines+=1
        print('Number of lines:', number_lines)
        print('Number of words:', number_words)
        

#A
count_lines_and_words('obama_speech.txt')

#B
count_lines_and_words('michelle_obama_speech.txt')