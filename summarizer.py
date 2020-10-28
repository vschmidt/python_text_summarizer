#Imports
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

from string import punctuation
from collections import defaultdict
from heapq import nlargest


# Paramns
sents_qtd = 4 #Quantity of sents in summary 
path = 'inputs/manifesto.txt' #Input path
new_path = 'outputs/word_freq.txt' #Output path

# Get file
file_ = open(path, 'r')
text = file_.read()
file_.close()

# NPL
sents = sent_tokenize(text)
words = word_tokenize(text)
stop_words = set(stopwords.words('portuguese') + list(punctuation))
words_stopwords_off = [w for w in words
                      if w not in stop_words] #Remove Stopwords


words_freq = FreqDist(words_stopwords_off) # Words count
important_sentences = defaultdict(int)

for i, sent in enumerate(sents):
    for word in word_tokenize(sent.lower()):
        if word in words_freq:
            important_sentences[i] += words_freq[word] 
            



idx_most_important = nlargest(
                                sents_qtd,
                                important_sentences,
                                important_sentences.get
)

# Make summary
summary_content = ''

for i in sorted(idx_most_important): #Print sentences
    summary_content += sents[i] + '\n\n'

# Export
file_ = open(new_path, 'w')
file_.writelines(summary_content)
file_.close()
