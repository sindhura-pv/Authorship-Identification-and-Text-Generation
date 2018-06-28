"""
From the gutenberg corpus available in nltk we take the works of 3 authors.
For each work we build and train a Unigram, Bigram and a Trigram model
Given a piece of test text, this code calculates the probability as to which one of the 3 Authors it belongs to.
It can also generate text similar to the work of a given author.
"""
from nltk.corpus import gutenberg
from itertools import chain
from math import log

from nltk.probability import (FreqDist, ConditionalProbDist,
    ConditionalFreqDist,
    LidstoneProbDist)
from nltk.util import ngrams
from nltk.model.api import ModelI
from nltk.model.ngram import NgramModel
from random import randint
from nltk.tokenize import word_tokenize
import numpy as np

est = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

noOfFiles = 3
fileids = ['bryant-stories.txt', 'carroll-alice.txt', 'shakespeare-hamlet.txt']
Authors = ['Bryant', 'Carroll', 'Shakespeare']
lenFirstSent = [len(gutenberg.sents(fileids[i])[0])-1 for i in range(noOfFiles)]
C = [gutenberg.words(fileids[i])[lenFirstSent[i]:] for i in range(noOfFiles)]
lenC = [len(C[i]) for i in range(noOfFiles)]

unigram = [NgramModel(1, C[i], estimator=est) for i in range(noOfFiles)]
bigram = [NgramModel(2, C[i], True, True, estimator=est) for i in range(noOfFiles)]
trigram = [NgramModel(3, C[i], True, True, estimator=est) for i in range(noOfFiles)]


def generateText(model, train):
    pos = []
    for i in range(20):
        pos.append(train[randint(0, len(train))])
    return model.generate(50, set(pos))


def modelEntropy():
    for i in range(noOfFiles):
        text = generateText(trigram[i],C[i])
        print(fileids[i], ':')
        print(unigram[i].entropy(text))
        print(bigram[i].entropy(text))
        print(trigram[i].entropy(text))


def identifyAuthor(text):
    words = word_tokenize(text)
    logprob = np.zeros([3, 3])
    for i in range(noOfFiles):
        logprob[i] = [(-1)*unigram[i].entropy(words)*len(words),
                        (-1)*bigram[i].entropy(words)*len(words),
                            (-1)*trigram[i].entropy(words)*len(words)]

    print("Author as predicted by the Unigram model: ", Authors[[i for i in range(3) if logprob[i, 0] == max(logprob[:,0])][0]])
    print("Author as predicted by the Bigram model: ", Authors[[i for i in range(3) if logprob[i, 1] == max(logprob[:,1])][0]])
    print("Author as predicted by the Trigram model: ", Authors[[i for i in range(3) if logprob[i, 2] == max(logprob[:,2])][0]])


def generateRandomText(i):
    print("unigram: \n", " ".join(generateText(unigram[i], C[i])))
    print("bigram: \n", " ".join(generateText(bigram[i], C[i])))
    print("trigram: \n", " ".join(generateText(trigram[i], C[i])))


def stats():
    for i in range(noOfFiles):
        print(fileids[i], ':')
        print('Number of types: ', len(C[i]))
        print('Number of tokens: ', len(set(C[i])))
