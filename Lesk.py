from re import S
from tracemalloc import stop
from turtle import pos
import filelock
import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pprint
nltk.download('punkt')
pos = []

def findSense(sense_words):
    for i in range(len(sense_words)):
        path_values_main= []
    for sense_word in sense_words:
        path_values = []
        max = 0
        temp1 = 0
        temp2 = 0
        synset1 = wn.synsets(sense_word)
        for sense_word2 in sense_words:
            synset2 = wn.synsets(sense_word2)
            if sense_word2 != sense_word:
                for i1 in range(len(wn.synsets(sense_word))):
                    for j1 in range(len(wn.synsets(sense_word2))):
                        temp = (synset1[i1]).path_similarity(synset2[j1])
                        if temp > max:
                            max = temp
                            temp1 = i1
                            temp2 = j1
            pos.append((temp1,temp2))
                            

        









sentences = []
corpus = "The Library issued a book.That woman's latest issue died."
sentences.extend(nltk.tokenize.sent_tokenize(corpus))
print(sentences)
# I have to find those words which have more than one synsets and find the corresponding word sense
# I can remove stopwords.
        
words = []

word_list = word_tokenize(corpus)
list_stop=[]

stop_words=set(stopwords.words('english'))
for i in word_list:
    l = i.lower()
    if l not in stop_words:
        list_stop.append(l)
# print("All NON Stop words:-")
# print(list_stop)
possible_words = []

# It is better if we Lemmatize the possible_words

from nltk.stem.porter import PorterStemmer
Stemmed_text = []
Port = PorterStemmer()
for word_stem in list_stop:
    Stemmed_text.append(Port.stem(word_stem))

from nltk.stem import WordNetLemmatizer
Lemma = WordNetLemmatizer()
Lemma_text = []
for word_lemma in Stemmed_text:
    Lemma_text.append(Lemma.lemmatize(word_lemma))


for word in list_stop:
    if len(wn.synsets(word)) > 1: 
        possible_words.append(word)
print(possible_words)


for sentence in sentences:
    temp_words = []
    sense_words = []
    pos = []
    temp_words = word_tokenize(sentence)
    for sen_words in temp_words:
        if sen_words in possible_words:
            sense_words.append(sen_words)
    findSense(sense_words)
    # print(type(pos))
    # print(type(pos[2][1]))
    for word in sense_words:
        synset1 = wn.synsets(word)
        max = 0
        for i in range(len(sense_words)):
            if pos[i][0] > max:
                max = pos[i][0]
        print("The meaning of ", word, "     is probably is:-    ", synset1[max].definition())


pprint.pprint(pos)


# The problem is with pos   

        
            # if the word in the sentence then find it's sense using other words in the sentence









            





    

 
