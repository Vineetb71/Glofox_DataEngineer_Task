# Glofox_DataEngineer_Task

### Table of contents
* [Introduction](#introduction)
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Algorithms](#algorithms)
* [Extra Features](#extra-features)


### Introduction
A simple job developed in python 3.0 which provides you with a word dictionary and an inverted index based on a collection of documents.

### General info
The basic criteria behind this job is to build an inverted index of the documents so that it can speed up calculations. Based on the task and being jon snow who is passionate about information search and data engineering this tool is built which can be used by various search engine where just by entering the word we can identify that this word is present in how many dcouments. This actually sounds interesting as this tool can create a word dictionary (mapping of word and word id) as well as an inverted index which maps each word id to a document id. So just by searching a word it will tell you in which document or a list of documents this word exists.

### Technologies

Task is created with:

* Python version: 3.0
* Testing .txt files created in sublime text.
* Tools used : Jupyter notebook and spyder to execute the python script

### Setup
* Any tool such as spyder/Pycharm can be used to run the python script.
* Installation guide to install spyder : https://docs.spyder-ide.org/current/installation.html
* Easiest way is to install anaconda navigator and use spyder from that.
* To test the functionality of the code some testing files are uploaded in the "Testing_Files" folder. All the files are with '.txt' extension same as original       dataset.
* The code is tested on the original datasets as well but just to include test cases these are attached in the repository.
* 'Glofox_Test.py' is the executable file for spyder or jupyter notebook which is included in the repository.
* All these text files and the 'Glofox_Test.py' file should be placed in the same directory on local machine so that it can be executed without much changes in the   path of directory required in the code.

### Algorithms

To develop the dictonary and inverted index simultaneously, a combination of `Blocked sort-based indexing`(BSBI)  and `Single-pass in-memory indexing` (SPIMI)
is used. 
BSBI is used to map the word with word_id and create a word dictonary while SPIMI is used to create a single flow in which word_id from the dictonary is mapped to the doc_id of the dataset. So during each successive call of SPIMI-INVERT, when a term occurs for the first time, it is added to the dictionary and a new postings list is created which will assign the current_doc_id to the word_id, instead of fetching the word, the word_id is mapped to the doc_id which is prime requirement 
of the task resulitng in final inverted index.
This process is fast enough and no such sorting is required while mapping as we are iterating through the indexes and appending them which are already sorted.

### Extra Features

* Additionally User interaction is added in the job. User has to enter a word which needs to be searched once word is entered the result will be displayed on screen   like : if the user is present in the dictonary or not. If it is present the word and corresponding id will be displayed plus for each word inverted matrix will     also be displayed stating the word_id and in which doc_id's the word is present.
* Feature which can be added here was importing a pyspark package and create a job that will do this automatically with some additional parameters to be introduced.
* Web app can be created by python flask or django framework so that only the app should be run on the screen and user can play along with app searching for their     word without having any interaction with the code just the UI for them.

