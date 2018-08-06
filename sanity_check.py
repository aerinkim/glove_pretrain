
# Sanity Check: Comparing the keys of the two vectors.
# It outputs "diff.txt" where you could locate the differences in two trained vectors.

g_840_=[]
g_wikipedia_=[]

def g_840():
	with open("g_840.txt", mode="w" , encoding="utf8") as outfile: 
		with open('../v1_squad_vteam/data/glove.840B.300d.txt', encoding="utf8") as f:
			for line in f:
				elems = line.split()
				token = ' '.join(elems[0:-300])
				outfile.write("%s\n" %(token))
				g_840_.append(token)

def g_wikipedia():
	with open("g_wiki.txt", mode="w" , encoding="utf8") as outfile: 
		with open('../GloVe/build/glove.Wikipedia4B.300d.txt', encoding="ISO-8859-1") as f:
			for line in f:
				elems = line.split()
				token = ' '.join(elems[0:-300])
				outfile.write("%s\n" %(token))
				g_wikipedia_.append(token)


g_840()
g_wikipedia()

i = 0
with open("diff.txt", mode="w" , encoding="utf8") as outfile: 
	for i in range(0,len(g_840_)):
		if g_840_[i] != g_wikipedia_[i]:
			#print (g_840_[i] , g_wikipedia_[i])
			outfile.write("%s %s %s\n" %(g_840_[i], g_wikipedia_[i], i))