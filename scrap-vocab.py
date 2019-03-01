"""
description: Getting vocabulory from a file

"""

import glob
import os
import json

NEWS_ARTICLES_FOLDER = "BBC-news-articles/News-Articles"
OUTPUT_FILE          = "vocab.txt"
STOP_WORDS           = "stopwords.txt"

def get_vocab():
    
    folders = glob.glob(os.path.join(NEWS_ARTICLES_FOLDER, '*'))
    files = []
    stop_words_dict = set()

    stop_file = open(STOP_WORDS, 'r')
    stop_data = stop_file.strip().split(',')
    for word in stop_data:
        stop_words.add(get_word(word))
    stop_file.close()
        
    for keys in stop_words_dict.keys():
        print("STOP WORD:", keys)
    
    for folder in folders:
        summaries = glob.glob(os.path.join(folder, '*'))
        files += summaries

    vocab = {}
    for each_file in files:
        get_vocab_from_file(each_file, vocab)

    list_vocab = []
    for j in vocab.keys():
        list_vocab.append([vocab[j], j])
    list_vocab.sort()

    
    file_to_write = open(OUTPUT_FILE, 'w')
    for index in range(len(list_vocab)-1, -1, -1):
        word = list_vocab[index]
        line = str(word[1]) + " " + str(word[0]) + '\n'
        file_to_write.write(line)
    file_to_write.close()
    print("Vocab scraped")
    
def get_vocab_from_file(filename, dic):
    file = open(filename, 'r')

    for line in file:
        line.encode('utf-8').strip()
        line = line.lower()
        words = line.strip().split()
        for word in words:
            word = get_word(word)
            if word:
                dic[word] = dic.get(word, 0) + 1
    file.close()
    
def get_word(word):
    if word:
        start = 0
        end = len(word)-1

        while start <= end:
            if word[start].isalnum():
                break
            else:
                start += 1

        while end >= 0:
            if word[end].isalnum():
                break
            else:
                end -= 1
        return word[start:end+1]

get_vocab()

        
