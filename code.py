from nltk.corpus import gutenberg
from itertools import chain
from math import log

from nltk.probability import (FreqDist,
    ConditionalProbDist,
    ConditionalFreqDist,
    LidstoneProbDist)
from nltk.util import ngrams
from nltk.model.api import ModelI
from nltk.model.ngram import NgramModel
from random import randint
from nltk.tokenize import word_tokenize

est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)



noOfFiles=3
fileids=['bryant-stories.txt','carroll-alice.txt','shakespeare-hamlet.txt']
lenFirstSent=[len(gutenberg.sents(fileids[i])[0])-1 for i in range(noOfFiles)]
C=[gutenberg.words(fileids[i])[lenFirstSent[i]:] for i in range(noOfFiles)]
lenC=[len(C[i]) for i in range(noOfFiles)]

unigram=[NgramModel(1,C[i],estimator=est) for i in range(noOfFiles)]
bigram=[NgramModel(2,C[i],True,True,estimator=est) for i in range(noOfFiles)]
trigram=[NgramModel(3,C[i],True,True,estimator=est) for i in range(noOfFiles)]

def generateText(model,train):
	pos=[]	
	for i in range(20):
		pos.append(train[randint(0,len(train))])
	return model.generate(50,set(pos))

def modelEntropy():
	for i in range(noOfFiles):
		text=generateText(trigram[i],C[i])
		print fileids[i],':'
		print unigram[i].entropy(text)
		print bigram[i].entropy(text)
		print trigram[i].entropy(text)

def identifyAuthor(text):
	words=word_tokenize(text)
	for i in range(noOfFiles):
		my_logprob=[0.0,0.0,0.0]			
		my_logprob[0]=(-1)*unigram[i].entropy(words)*len(words)	
		my_logprob[1]=(-1)*bigram[i].entropy(words)*len(words)
		my_logprob[2]=(-1)*trigram[i].entropy(words)*len(words)
		print fileids[i],': Unigram: ',my_logprob[0],' Bigram: ',my_logprob[1],' Trigram: ',my_logprob[2]

def generateRandomText(i):
	print "unigrams \n"," ".join(generateText(unigram[i],C[i]))	
	print "bigrams \n"," ".join(generateText(bigram[i],C[i]))
	print "trigrams \n"," ".join(generateText(trigram[i],C[i]))

def stats():
	for i in range(noOfFiles):
		print fileids[i],':'
		print 'Number of types: ',len(C[i])
		print 'Number of tokens: ',len(set(C[i]))