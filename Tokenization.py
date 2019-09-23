# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 03:09:18 2019

@author: Dilip
"""

import nltk

paragraph= """Before taking about machine learning let's talk about another concept is called data mining. 
              Data mining is a technique of examining a large pre existing database end extracting new information from that database. 
              It's easy to understand, right, machine learning does the same,in fact, machine learning is a type of data mining technique.

              Here's is the basic meaning of machine learning:

              “Machine learning is a technique of parsing data, learn from that data and then apply what they have learned to make an informed decision”

              Now a days many of big companies use machine learning to give there users a better experience, some of the examples are , 
              Amazon using machine learning to give better product choice recommendations to there costumers based on their preferences, 
              Netflix usa machine learning to give better suggestions to their users of the TV series or movies or shows that they would like to watch."""
              
#tokenize the sentences 
sentences=nltk.sent_tokenize(paragraph)

#tokenize the words
words=nltk.word_tokenize(paragraph)            
              