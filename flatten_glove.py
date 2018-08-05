def flatten_glove():

	i=0
	with open("../GloVe/build/flattened.glove.840d.300.txt", mode="w" , encoding="utf8" ) as outfile: 
		with open('../v1_squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
			for line in f:
				tokens = line.split() # Removing the word (key) and write only values
				#print(mylist[0])
				#if len(mylist) != 300:
				#	print(i, line.split()[0])
				dimensions = tokens[-300:]

				for s in dimensions:
				
					try:
					    s=float(s)/2
					    outfile.write("%s\n" % s)
					except ValueError:
					    print ("Not a float")

				i+=1

if __name__ == '__main__':
	flatten_glove()
