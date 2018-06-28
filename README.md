# Authorship estimation and Text generation
Objective

To build Unigram, Bigram and Trigram language models to predict the probability that a given piece of test text belongs 
to the work of a particular author. Also to generate a small text similar to the work of a given author.

Software Requirements

Python 3

Natural Language Tool Kit

Download the gutenberg corpus using the command nltk.download()

Usage

Menu.py is the front end of a Text generation and Authorship estimation project. Run this code and enter a number based on the functionality you desire. It calls the corresponding function in the code.py file and gives the result.

Project Description

From the gutenberg corpus available in nltk we take the works of 3 authors namely Bryant, Carroll and Shakespeare.
For each work we build and train a Unigram, Bigram and a Trigram model.
Given a piece of test text, this code calculates the unigram, bigram and trigram probabilities as to which one of the 3 Authors it belongs to.
It can also generate text similar to the work of a given author based on the uni, bi and trigram models built using the corpus of their work.

