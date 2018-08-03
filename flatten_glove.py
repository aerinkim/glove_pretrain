def flatten_glove():
	i=0
	with open("flattened.glove.840d.300.txt", mode="w") as outfile: 
		with open('../squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
			for line in f:
				tokens = line.split() # Removing the word (key) and write only values
				#print(mylist[0])
				#if len(mylist) != 300:
				#	print(i, line.split()[0])
				tokens = tokens[-300:]
				for s in tokens:
					if s.isdigit():
						s=float(s)/2
						outfile.write("%s\n" % s)
					else:
						raise ValueError('is not digit!')
				i+=1

if __name__ == '__main__':
	flatten_glove()
