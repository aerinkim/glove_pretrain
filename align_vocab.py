
# We have to align the sequence of vocab.txt as same as glove.840d.300.txt

# Also  glove.840d.300.txt contains duplicated keys. We have to remove them.


def create_new_vocab_txt(unigram_count_dictionary):
	unigram_count_dictionary = create_unigram_count_dictionary() 
	# We have to align the sequence of vocab.txt as same as glove.840d.300.txt
	with open("../GloVe/build/new_vocab.txt", mode="w" , encoding="utf8") as outfile: 
		with open('../v1_squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
			i=0 # for loop index
			j=0 # To prevent duplicate words we put integer at the end of the word. 
			tokens_seen_before=set()
			tokens_seen_before.add('')
			for line in f:
				elems = line.split()

				if len(elems) != 301:
					print ('This token is not one word!',i, elems[:-300])
				
				token = '_'.join(elems[0:-300])

				if token in tokens_seen_before:
					token = token+'__'+str(j)+'__'
					j+=1
				else:
					tokens_seen_before.add(token)

				if token in unigram_count_dictionary.keys():
					val = unigram_count_dictionary[token]
				else:
					#print (token," is not found!")
					val = 10
				outfile.write("%s %s\n" %(token, val ))
				i+=1


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