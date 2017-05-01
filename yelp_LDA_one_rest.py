import json
import operator

#import packages for LDA
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import Stop_words_en
import string

top3Json = [json.loads(line) for line in open("top3.json", "r", encoding = 'utf-8')]


#Restaurant is in the form of (business_id: [business object, ["review1", "review 2" ...], num_rev])
def run_LDA(restaurant):
	#Information on the top restaurant with the most reviews 
	top_one_name = restaurant[1][0]
	top_one_reviews = restaurant[1][1]
	top_one_num_revs = restaurant[1][2]
	top_one_rev_dist = {1:0, 2:0, 3:0, 4:0, 5:0}

	#Set up for LDA
	tokenizer = RegexpTokenizer(r'\\w+')
	en_stop = Stop_words_en.make_stop_bigger()
	p_stemmer = PorterStemmer()

	Test = [[],[],[],[],[]] 

	for review in top_one_reviews:
		stars = review['stars']
		if stars in top_one_rev_dist:
			top_one_rev_dist[stars] += 1 

		review_lower = review['text'].lower()
		review_lower = review_lower.translate(review_lower.maketrans({key: None for key in string.punctuation}))                          # Output: string without punctuation
		tokens = review_lower.split(" ")
		stopped_tokens = [i for i in tokens if not i in en_stop]
		stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
		Test[int(stars)-1].append(stemmed_tokens)

	print("Business name: " + top_one_name['name'])
	print("Business Rating Dist: " + str(top_one_rev_dist))
	for star in Test:			
		if len(star) > 10:
			# turn our tokenized documents into a id <-> term dictionary
			dictionary = corpora.Dictionary(star)
			# convert tokenized documents into a document-term matrix
			corpus = [dictionary.doc2bow(text) for text in star]
			# generate LDA model
			ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=10)
			topics = ldamodel.print_topics(num_topics=3, num_words=5)
			print(str(Test.index(star)+1) + " Star reviews" )
			print("Topics: ")
			print(topics)
		
	
restaurant = 2 
run_LDA(top3Json[0][restaurant])
