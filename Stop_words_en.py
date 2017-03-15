from stop_words import get_stop_words

#stop_words = get_stop_words("en")

#custom = ["word", "one", "work", "get", "even"]

def make_stop_bigger():
	stop_words = get_stop_words("en")
	custom = ["word", "one", "work", "get", "even", "just", "lot", "look", "place", "bit", "help", "time", "simpl", "also", ".", "-"]
	stop_words += custom
	return stop_words

def add_stop_words(stop_words, word):
	stop_words.append(word)

def get_me_stop_words():
	return stop_words