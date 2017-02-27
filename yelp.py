import json

#import packages for LDA
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

files = ["yelp_academic_dataset_business.json",
    		"yelp_academic_dataset_checkin.json",
    		"yelp_academic_dataset_review.json",
    		"yelp_academic_dataset_user.json"]


file = open("yelp_academic_dataset_checkin.json", "r")
    #Load data
business = [json.loads(line) for line in open(files[0], "r", encoding = 'utf-8')]
# checkin = [json.loads(line) for line in open(files[1], "r")]
review = [json.loads(line) for line in open(files[2], "r", encoding='utf-8')]
# user = [json.loads(line) for line in open(files[3], "r")]

#append all reviews to dictionary of businesses
# allbid = {b['business_id']: [] for b in business}
fourplus = {}
fourminus = {}
for rev in review:
    if rev['stars'] >= 4:
        if rev['business_id'] in fourplus.keys():
            fourplus[rev['business_id']].append(rev)
        else:
            fourplus[rev['business_id']] = [rev]
    elif rev['stars'] < 4:
        if rev['business_id'] in fourminus.keys():
            fourminus[rev['business_id']].append(rev)
        else:
            fourminus[rev['business_id']] = [rev]
tokenizer = RegexpTokenizer(r'\\w+')
en_stop = get_stop_words('en')

p_stemmer = PorterStemmer()

#Test business to analyze
# testbis = list(allbid.values())[0]
testone = list(fourplus.values())[0]
testtwo = list(fourminus.values())[0]

positivedocs = []
negativedocs = []
for review in testone:
    lowerRev = review['text'].lower()
    tokens = lowerRev.split(" ")
    tokens = [k for k in tokens if k != "" and k != "," and not k.isdigit()]
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    positivedocs.append(stemmed_tokens)
for review in testtwo:
    lowerRev = review['text'].lower()
    tokens = lowerRev.split(" ")
    tokens = [k for k in tokens if k != "" and k != "," and not k.isdigit()]
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    negativedocs.append(stemmed_tokens)
# turn our tokenized documents into a id <-> term dictionary
dictionary_one = corpora.Dictionary(positivedocs)
dictionary_two = corpora.Dictionary(negativedocs)
# convert tokenized documents into a document-term matrix
corpus = [dictionary_one.doc2bow(text) for text in positivedocs]
corpus_two = [dictionary_two.doc2bow(text) for text in negativedocs]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary_one, passes=10)
ldamodel_2 = gensim.models.ldamodel.LdaModel(corpus_two, num_topics=2, id2word = dictionary_two, passes=10)

print(ldamodel.print_topics(num_topics=2, num_words=4))
print(ldamodel_2.print_topics(num_topics=2, num_words=4))
