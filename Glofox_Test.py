#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:46:43 2020

@author: Vineet Bhatnagar
Project Name : Game of thrones - Inverted Index calculation
"""
import codecs
import string
import glob
import re

#Function to create Inverted Index
def Inverted_Index (file_list) :
    
    #Declaring the variables used in the program
    doc_map ={}
    word_dic = {}
    inverted_index = {}
    doc_id = 0
    word_id = 0
    
    #Sorting for each txt extension file by digits
    file_list.sort(key=lambda f: int(re.sub('\D', '', f)))
    
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
           
           #Checking if word already existing in the word_dic (dictionary), if so 
           #fetching the word_id from the word_dic and appending the current_doc_id to 
           #the existing mapped list.
           
           if (word in word_dic) :
               current_word_id = word_dic.get(word)
               int_list = inverted_index.get(current_word_id) 
               if current_doc_id not in int_list :
                    int_list.append(current_doc_id)
                    
           #This code will only be executed when there is a unique word in a doc. 
           #This block assigns a unique word id to each word and add it to
           #the word dictionary (word_dic).
           #adding currentdocid in a posting list and assigning it to a currentwordid as a part of creating
           #an inverted index based on wordid and docid mapping.
            
           else :
               current_word_id = word_id
               word_id = word_id + 1 
               word_dic[word] = current_word_id
               int_list =[]
               int_list.append(current_doc_id)
               inverted_index[current_word_id] = int_list 
               
    #Closing a particular file    
    text_file.close()  
    
    #printing the word dictionary  
    print("\nThe unique dictonary\n")
    for key,value in word_dic.items() : 
        print('{0: <10}'.format(key),'%20s' % value)
		 
    print("\nThe final inverted index\n") 
    #Printing the final inverted index 
    for key,value in inverted_index.items() :
        print("(" + str(key) + ",",str(value) + ")\n")
		
    # Additional part to search the word and it's reference documents based on the input given  
    val = input("Enter the word you want to search: \n") 
    if val in word_dic.keys():
        print("\nThe searched word is {""} and it is available in dictionary\n".format(val))
        print('{0: <10}'.format(val),'%10s\n' % word_dic[val])
        if word_dic[val] in inverted_index.keys():
            print("Inverted index is as follows:\n".format(val))
            print("(" + str(word_dic[val]) + ",",str(inverted_index[word_dic[val]]) + ")\n")
            
    else:
        print("The word is not present in the dictionary or any text file")
            
 
if __name__ == "__main__":
    
    #Calling the function to calculate Inverted Index
    Inverted_Index(file_list = glob.glob('*.txt'))      
   
    
    
    
    
