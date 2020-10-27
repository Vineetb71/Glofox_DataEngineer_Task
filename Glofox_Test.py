#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:46:43 2020

@author: Vineet Bhatnagar
"""
#import packages
import codecs
import string
import glob

#start of the program

if __name__ == "__main__":
    
    #Declaring the variables used in the program
    
    doc_map ={}
    word_dic = {}
    word_map = {}
    inverted_index = {}
    int_list =[]
    doc_id = 0
    word_id = 0
    
    #Iterating for each txt extension file
    file_list = glob.glob('*.txt')
    file_list.sort()
    
    for current_file in file_list:
        
        #Checking if the document already exists if so continue and rerun the for loop
        if current_file in doc_map:
            continue      
        
        #Opening a particular text file and reading the current doc id in docmap list
        text_file = codecs.open(current_file,"r","cp1252")
        current_doc_id = doc_id
        doc_id = doc_id + 1
        doc_map[current_file] = current_doc_id
        for word in text_file.read().split():
           
           #Removing unnecessary punctuation from the words
           word = word.translate(str.maketrans('', '', string.punctuation))
           word = word.lower()
           
           #Checking if word already existing in the word_map (dictionary), if so 
           #fetching the word_id from the word_dic and appending the current_doc_id to 
           #the existing mapped list containing the word_id and doc_id posting list.
           
           if (word in word_map) :
               current_word_id = word_map.get(word)
               int_list = inverted_index.get(current_word_id) 
               if current_doc_id not in int_list :
                    int_list.append(current_doc_id)
                    
           #This code will only be executed when there in a unique word in a doc 
           #This block assigns a unqique word id to each word and add it to
           #the word dictionary, simultaneously creating a worddicindex to hold id as a key.
           #Fetching currentdocid and assigning it to a currentwordid as a part of creating
           #an inverted index based on wordid and docid mapping.
            
           else :
               current_word_id = word_id
               word_id = word_id + 1 
               word_map[word] = current_word_id
               word_dic[current_word_id] = word
               int_list =[]
               int_list.append(current_doc_id)
               inverted_index[current_word_id] = int_list 
        
    text_file.close()  
    
    #printing the word dictionary  
    print("\nThe unique dictonary\n")
    for key,value in word_dic.items() :
        {
			print('{0: <10}'.format(value),'%15s' % key)
		}
    
    
    print("\nThe merged inverted index\n")
    #Printing the final inverted index 
    for key,value in inverted_index.items() :
        {
			print("(" + str(key) + ",",str(value) + ")\n")
		}
        
        
