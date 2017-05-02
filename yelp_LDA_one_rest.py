import json
import operator

#import packages for LDA
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import Stop_words_en
import string
import numpy as np


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
	unique_stemmed_words =[{},{},{},{},{}]
	all_rev = [[],[],[],[],[]]
	for review in top_one_reviews:
		stars = review['stars']
		if stars in top_one_rev_dist:
			top_one_rev_dist[stars] += 1 

		review_lower = review['text'].lower()
		review_lower = review_lower.translate(review_lower.maketrans({key: None for key in string.punctuation}))                          # Output: string without punctuation
		tokens = review_lower.split(" ")
		# stopped_tokens = [i for i in tokens if not i in en_stop]
		stemmed_tokens = [p_stemmer.stem(i) for i in tokens if i not in en_stop]
		all_rev[int(stars)-1].append((review['text'], stemmed_tokens))
		for word in stemmed_tokens:
			d = unique_stemmed_words[int(stars) - 1]
			if word in d:
				d[word] += 1
			else:
				d[word] = 1
		Test[int(stars)-1].append(stemmed_tokens)
	print("Step 1")
	return [unique_stemmed_words, all_rev]
	# print("Business name: " + top_one_name['name'])
	# print("Business Rating Dist: " + str(top_one_rev_dist))
	# for star in Test:			
	# 	if len(star) > 10:
	# 		# turn our tokenized documents into a id <-> term dictionary
	# 		dictionary = corpora.Dictionary(star)
	# 		# convert tokenized documents into a document-term matrix
	# 		corpus = [dictionary.doc2bow(text) for text in star]
	# 		# generate LDA model
	# 		ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word = dictionary, passes=10)
	# 		topics = ldamodel.print_topics(num_topics=3, num_words=5)
	# 		print(str(Test.index(star)+1) + " Star reviews" )
	# 		print("Topics: ")
	# 		print(topics)
def term_frequency(word, tokenized_str):
    return tokenized_str.count(word)
def idf_values(tokenized_users, term_index):
    val = {}
    for word in term_index:
        #print("doing stuff " + word)
        count = 0
        for rev in tokenized_users:
        	if word in rev:
        		count += 1
        # count = sum([1 for x in tokenized_users if word in tokenized_users])
        idf = np.log(len(term_index.keys()) / (count + 1))
        val[word] = idf
        #print("idf: " + str(idf))
    return val
def similarity(word_vector, query_vector):
    #print(word_vector.shape)
    #print(query_vector.shape)
    sim = np.dot(word_vector, query_vector)[0][0]
    #print(sim)
    return sim
def tf_idf(tokenized_users, query, term_index):
    print("Step 1.5")
    idf_dict = idf_values([set(x[1]) for x in tokenized_users], term_index)
    all_users_tfidf = []
    print("Step 2")
    for user, tokens in tokenized_users:
        #print("Step 3")
        user_tfidf = []
        #print(user + " " + str(tokens))
        if len(tokens) == 0:
            continue
        for word in idf_dict.keys():
            freq = term_frequency(word, tokens) / len(tokens)
            user_tfidf.append(freq * idf_dict[word])
        all_users_tfidf.append((user, np.array([user_tfidf]).T))

    print("Step 4")
    search_vector = []
    for word in idf_dict.keys():
        freq = term_frequency(word, query) / len(query)
        search_vector.append(freq * idf_dict[word])
    #print('numpying')
    search_vector = np.array([search_vector])
    # for i in all_users_tfidf:
    # 	i[1] = np.array([i[1]]).T
    #print("computing max")
    return max(all_users_tfidf, key = lambda x: similarity(x[1], search_vector))
    # return [tup[0] for tup in sorted(all_users_tfidf, key = lambda x: similarity(x[1], search_vector), reverse=True)]		


restaurant = 0
answer = run_LDA(top3Json[0][restaurant])
print(len(answer[0][4]))
#print(tf_idf(answer[1][4], ["great", "food", "steak", "vega","bellagio"], answer[0][4])[0])
#print("3stars: " + tf_idf(answer[1][2], ["food", "tabl", "good", "servic","great"], answer[0][2])[0])
print("1star: " + tf_idf(answer[1][0], ["food", "wait", "us", "tabl","servic"], answer[0][0])[0])
print("2stars: " + tf_idf(answer[1][1], ["food", "order", "tabl", "us","restaur"], answer[0][1])[0])
print("4stars: " + tf_idf(answer[1][3], ["good", "breakfast", "egg", "great","servic"], answer[0][3])[0])





