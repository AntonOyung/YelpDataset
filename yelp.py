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
business = [json.loads(line) for line in open(files[0], "r")]
checkin = [json.loads(line) for line in open(files[1], "r")]
review = [json.loads(line) for line in open(files[2], "r")]
user = [json.loads(line) for line in open(files[3], "r")]

    #append all reviews to dictionary of businesses
allbid = {b['business_id']: [] for b in business}

for rev in review:
    allbid[rev['business_id']].append(rev)
tokenizer = RegexpTokenizer(r'\\w+')
en_stop = get_stop_words('en')

p_stemmer = PorterStemmer()

    #Test business to analyze
testbis = allbid[0]

texts = []
for review in testbis:
    lowerRev = review['text'].lower()
    tokens = tokenizer.tokenize(lowerRev)

stopped_tokens = [i for i in tokens if not i in en_stop]
stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
texts.append(stemmed_tokens)
