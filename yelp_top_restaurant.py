import json
import operator

#import packages for LDA
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


file = open("data.json", "r")
#Load data

#business = [json.loads(line) for line in open(restaurants[0], "r", encoding = 'utf-8')]

Andrewjson = [json.loads(line) for line in open("data.json", "r", encoding = 'utf-8')]

#append all reviews to dictionary of businesses
# allbid = {b['business_id']: [] for b in business}

sorted_Andrew = sorted(Andrewjson.items(), key = operator.itemgetter(2))

#Format of our sorted dictionary
#sorted = (business_id: ["name of restaurant", ["review1", "review 2" ...], num_rev])

#Information on the restaurant with the most reviews
top_one_name = sorted_Andrew[0].keys(0)
top_one_reviews = sorted_Andrew[0].keys(1)
top_one_num_revs = sorted_Andrew[0].keys(2)


#Set up for LDA
tokenizer = RegexpTokenizer(r'\\w+')
en_stop = get_stop_words('en')

p_stemmer = PorterStemmer()

TEST = []

for review in top_one_reviews:
    lowerRev = review['text'].lower()
    tokens = lowerRev.split(" ")
    tokens = [k for k in tokens if k != "" and k != "," and not k.isdigit()]
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    positivedocs.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(TEST)
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in TEST]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=10)

print(ldamodel.print_topics(num_topics=2, num_words=4))
