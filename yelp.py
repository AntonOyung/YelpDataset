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
allbid = {b['business_id']: [] for b in business}

for rev in review:
    allbid[rev['business_id']].append(rev)
tokenizer = RegexpTokenizer(r'\\w+')
en_stop = get_stop_words('en')

p_stemmer = PorterStemmer()

#Test business to analyze
testbis = list(allbid.values())[0:10]

texts = []

for reviews in testbis:
    for review in reviews:
        lowerRev = review['text'].lower()
        tokens = lowerRev.split(" ")
        tokens = [k for k in tokens if k != "" and k != "," and not k.isdigit()]
        stopped_tokens = [i for i in tokens if not i in en_stop]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        texts.append(stemmed_tokens)
# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=3, num_words=3)) 
