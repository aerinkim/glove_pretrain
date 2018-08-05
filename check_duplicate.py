
def check_duplicate():
	set_=set()
	with open('../GloVe/build/new_vocab.txt', encoding="utf8") as f:
		for line in f:
			elems = line.split()
			token = '_'.join(elems[0:-1])
			if token in set_:
				print ("dup", token)
			else:
				set_.add(token)


def check_duplicate2():
	set_=set()
	with open('../v1_squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
		for line in f:
			elems = line.split()
			token = '_'.join(elems[0:-300]) 
			if token in set_:
				print ("dup", token)
			else:
				set_.add(token)

print("#################################### Below are new_vocab.txt duplicates")
check_duplicate()
