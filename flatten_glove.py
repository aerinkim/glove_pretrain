import pickle


def flatten_glove(path):

	with open("flattened.glove.840d.300.txt", mode="w") as outfile: 

		with open('Glove.840d.300.txt', encoding="utf8") as f:
			for line in f:
				mylist = line.split()[1:] # Removing the word (key) and write only values
			    for s in mylist:
			        outfile.write("%s\n" % s)

if __name__ == '__main__':
	flatten_glove()
