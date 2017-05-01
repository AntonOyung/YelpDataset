import json
import operator

#import packages for LDA
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import Stop_words_en
import string

#Restaurant is in the form of (business_id: [business object, ["review1", "review 2" ...], num_rev])
def run_LDA(restaurant):
	#Information on the top restaurant with the most reviews 
	top_one_name = restaurant[0]
	top_one_reviews = restaurant[1]
	top_one_num_revs = restaurant[2]
	top_one_rev_dist = {1:0, 1.5:0, 2:0, 2.5:0, 3:0, 3.5:0, 4:0, 4.5:0, 5:0}

	#Set up for LDA
	tokenizer = RegexpTokenizer(r'\\w+')
	en_stop = Stop_words_en.make_stop_bigger()
	p_stemmer = PorterStemmer()

	TEST = []

	for review in top_one_reviews:
		stars = review['stars']
		if stars in top_one_rev_dist:
			top_one_rev_dist[stars] += 1 

		review_lower = review['text'].lower()
		review_lower = review_lower.translate(review_lower.maketrans({key: None for key in string.punctuation}))                          # Output: string without punctuation
		tokens = review_lower.split(" ")
		stopped_tokens = [i for i in tokens if not i in en_stop]
		stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
		TEST.append(stemmed_tokens)

	# turn our tokenized documents into a id <-> term dictionary
	dictionary = corpora.Dictionary(TEST)
	# convert tokenized documents into a document-term matrix
	corpus = [dictionary.doc2bow(text) for text in TEST]

	# generate LDA model
	ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=10)
	print("Business name: " + top_one_name['name'])
	print("Business Rating Dist: " + str(top_one_rev_dist))
	print("Topics: ")
	print(ldamodel.print_topics(num_topics=5, num_words=10))