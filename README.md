# Glofox_DataEngineer_Task

### Table of contents
* [Introduction](#introduction)
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithms](#algorithms)
* [Extra Features](#extra-features)


### Introduction
A simple job developed in python 3 which provides you with a word dictionary and an inverted index based on a collection of documents.

### General info
The basic criteria behind this job is to build an inverted index which maps every word to its respective document and gives a clear picture of exitence of each word in collection of documents. This is achieved by playing with their id's rather than word itself. Based on the task and being jon snow who is passionate about information search and data engineering this tool is built where just by entering the word you can identify that this word is present in which of the document. This actually sounds interesting as this job can create a word dictionary (mapping of word and word id) as well as an inverted index which maps each word id to a document id. So just by searching a word it will tell you in which document or a list of documents this word exists. Indexes are used just to speed up the process and it consumes less memory as well.

### Technologies

Task is created with:

* Python version: 3
* `.txt` files for testing are created in sublime text.
* Tools used : spyder 3.3.6 to code and execute the python script

### Setup
* Any tool such as spyder/Pycharm can be used to run the python script.
* Installation guide to install spyder : https://docs.spyder-ide.org/current/installation.html
* Easiest way is to install anaconda navigator and use spyder from that.
* To test the functionality of the code some testing files are uploaded in the "Testing_Files" folder. All the files are with '.txt' extension same as original       dataset.
* The code is tested on the original datasets as well but just to include test cases these are attached in the repository.
* 'Glofox_Test.py' is the executable file for spyder or jupyter notebook which is included in the repository.
* All these text files and the 'Glofox_Test.py' file should be placed in the same directory on local machine so that it can be executed without much changes in the   path of directory required in the code.

### Algorithms

To develop the dictonary and inverted index simultaneously, some part of `Single-pass in-memory indexing` (SPIMI) is used and basics of `Blocked sort-based indexing`(BSBI) are referred. Now what is an inverted index ?
* An inverted index is basically an index data structure storing a mapping from content, such as words or word_id's, to its locations in a document or a set of documents. It directs us from a word to a document or list of documents. In this task a `record-level inverted index` is used which contains a list of references to documents for each word.
* So to achieve the above, the steps followed are: Map the word with word_id and create a word dictionary for each doc on the fly and by using a single flow the word_id from the dictionary is mapped to the doc_id of the dataset. So during each recursion of docs , when a term occurs for the first time, it is added to the dictionary and simultaneously a new postings list is created which contains the current_doc_id. This id is then assigned to the current_word_id and it grows dynamically thereafter. Here the word_id is mapped to the doc_id or list of doc_id's based on the requirement of the task resulting in final inverted index. This is termed as inverted index because the wordid's are used to check its existence in documents rather then a document is used to check the availablity of words.
* This process is fast enough and no such sorting is required while mapping as we are iterating through the indexes and appending them which are already sorted.

### Extra Features

* Additionally User interaction is added in the job. User has to enter a word which needs to be searched once word is entered the result will be displayed on screen   like : if the user is present in the dictonary or not. If it is present the word and corresponding id will be displayed plus for each word inverted index will       also be displayed stating the word_id and in which doc_id's the word is present.
* Web app can be created by python flask or django framework so that only the app should be run on the screen and user can play along with app searching for their     word without having any interaction with the code just the UI for them.
* The stop words like 'is','are','the','am' etc. can also be removed programatically from the dictionary if required.
* Hadoop can be used to create jobs which can build blocked sort-based indexing algorithm in a much efficient way  containing the inbuilt functionality for       creating the block of docs, sorting and further merging the indexes. It works well on distributed system and much fater than others.

