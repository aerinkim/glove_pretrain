
# Align the key sequence of new_vocab.txt with voacb.txt

def create_new_vocab_txt(unigram_count_dictionary):
	unigram_count_dictionary = create_unigram_count_dictionary() 

	# We have to align the sequence of vocab.txt as same as glove.840d.300.txt
	with open("new_vocab.txt", mode="w") as outfile: 
		with open('../squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
			for line in f:
				key = line.split()[:1] # only getting the word (key) 

				if key[0] in unigram_count_dictionary.keys():
					val = unigram_count_dictionary[key[0]]
				else:
					print (key," is not found!")
					val = 10
				outfile.write("%s %s\n" %(key[0], val ))


def create_unigram_count_dictionary():
	unigram_count_dictionary = dict()
	with open('../GloVe/build/vocab.txt', encoding="utf8") as f:
		for line in f:
			key_value = line.split()[:2]
			unigram_count_dictionary[key_value[0]] = key_value[1]
	return unigram_count_dictionary


if __name__ == '__main__':
	unigram_dict = create_unigram_count_dictionary()
	create_new_vocab_txt(unigram_dict)