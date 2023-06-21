# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 22:21:42 2023

@author: Lenovo
"""

def most_frequent(string):
    freq_dict = {}
    
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    sorted_dict = sorted(freq_dict.items(), key=get_frequency, reverse=True)
    

    for item in sorted_dict:
        print(f"{item[0]} = {item[1]:02d}", end=" ")
        
def get_frequency(item):
    return item[1]

most_frequent("Mississippi")