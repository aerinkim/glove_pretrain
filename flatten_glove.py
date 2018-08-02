def flatten_glove():
	with open("flattened.glove.840d.300.txt", mode="w") as outfile: 
		with open('../squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
			for line in f:
				mylist = line.split()[1:] # Removing the word (key) and write only values
				for s in mylist:
					outfile.write("%s\n" % s)

if __name__ == '__main__':
	flatten_glove()
