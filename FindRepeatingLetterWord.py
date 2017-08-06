# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:49:22 2017

@author: user
"""

def find_word_repeating_char(str):
    str = str.lower()
    new_str = []
    for word in (str.split()):
        c = word[0]
        let=1
        while let < len(word):
            if c==word[let]:
                new_str.append(word)
            let += 1
    return new_str

str = "My name is Adity, Pop, Lol, Bob, Baby"
new_str = find_word_repeating_char(str)
print (new_str)