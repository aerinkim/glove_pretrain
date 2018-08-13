import numpy as np
from tokenizer import normalize_text

def creat_np_array_from_word2vec():
	arr = np.zeros(shape=(3000000,300))
	with open('../data/GoogleNews-vectors-negative300.txt', encoding="utf8") as f:
		i=0
		token_list = []
		for line in f:
			elems = line.split()
			arr[i] = [float(v) for v in elems[-300:]]
			i+=1
			if len(elems[0:-300]) ==1:
				parsed_tokens = elems[0:-300][0].split('_')
			else:
				print("non legit token")
				#print(line)
				print(elems[0:-300])
				parsed_tokens = ['___']	
			token = normalize_text(' '.join(parsed_tokens))
			token_list.append(token)
	return arr, token_list

def write_a_post_processed_word2vec(arr, token_list):
	with open("../data/GoogleNews-vectors-negative300_tokened.txt", mode="w" , encoding="utf8") as outfile: 
		for i in range(0,len(token_list)):
			token = token_list[i]
			dim_300 = ' '.join(str(j) for j in arr[i]) 
			outfile.write("%s %s\n" %(token, dim_300))
			if i % 100000 == 0:
				print ("write file:%s %s %s\n" %(str(i), token, dim_300))


if __name__ == '__main__':
	arr, token_list = creat_np_array_from_word2vec()
	write_a_post_processed_word2vec(arr, token_list)
