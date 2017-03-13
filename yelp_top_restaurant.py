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

#<<<<<<< HEAD

Andrewjson = [json.loads(line) for line in open("data.json", "r", encoding = 'utf-8')]


num_rev_dict = {}
# =======
# Andrewjson = None
# #Andrewjson = [json.loads(line) for line in open("data.json", "r", encoding = 'utf-8')]
# with open('data.json') as json_data:
#     Andrewjson = json.load(json_data)
# #append all reviews to dictionary of businesses
# # allbid = {b['business_id']: [] for b in business}
#
# sorted_Andrew = max([Andrewjson[k][1] for k in list(Andrewjson.keys())], key = lambda x: len(Andrewjson[x][1]))
# >>>>>>> 7775141e66019a719964b0471951f09128e59489

for business in Andrewjson:
    num_rev_dict[business] = Andrewjson[business][2]

sorted_num_rev_dict = sorted(num_rev_dict.items(), key = operator.itemgetter(1))

#sorted_Andrew = max([Andrewjson[0][k][1] for k in list(Andrewjson[0].keys())], key = lambda x: len(Andrewjson[0][x][1]))
sorted_Andrew = Andrewjson[sorted_num_rev_dict[0][0]]
#Format of our sorted dictionary
#sorted = (business_id: ["name of restaurant", ["review1", "review 2" ...], num_rev])

#Information on the restaurant with the most reviews
top_one_name = sorted_Andrew[0]
top_one_reviews = sorted_Andrew[1]
top_one_num_revs = sorted_Andrew[2]


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
