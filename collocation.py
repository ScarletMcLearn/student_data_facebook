import nltk
from nltk.collocations import *

#count single word frequency
f = open('aamir.txt')
raw = f.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
#bgs = nltk.bigrams(tokens)

#compute frequency distribution for all the words in the text
fdist = nltk.FreqDist(tokens)
for k,v in fdist.items():
    if v>=3:
    	print(k,v)
print('\n')
#bigram and trigram count
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# change this to read in your data
finder = BigramCollocationFinder.from_words(
   nltk.corpus.genesis.words('aamir.txt'))
finder1 = TrigramCollocationFinder.from_words(nltk.corpus.genesis.words('aamir.txt'))

# only bigrams that appear 3+ times
finder.apply_freq_filter(2) 
finder1.apply_freq_filter(1)


# return the 10 n-grams with the highest PMI
token = finder.nbest(bigram_measures.pmi, 10)
token1 = finder1.nbest(trigram_measures.pmi, 10)
#print(finder.ngram_fd.viewitems())
for item in token:
	print(item)
	#print(token.count(item))
#for k,v in finder.ngram_fd.items():
      #print(k,v)
print('\n')
for item in token1:
	print(item)
#print(token2)