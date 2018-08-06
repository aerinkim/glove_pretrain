

# Training Glove with pre-trained vectors 

Do you want to adapt the word embedding to your own specific corpus? 

One option is to train your own vectors by initializing it with Glove.840B.300d.txt . 

840B means that vector is trained on 840 Billion(!) tokens already. Given that the whole Wikipedia corpus consists of only 4 Billion tokens, you *don't* want to train your own vector with a tiny corpus and let go of the pretrained vector with 840 Billion tokens which is already available. 

### Package Contents

To train your own GloVe vectors, first you'll need to prepare your corpus as a single text file with all words separated by one or more spaces or tabs. If your corpus has multiple documents, the documents (only) should be separated by new line characters. Cooccurrence contexts for words do not extend past newline characters. Once you create your corpus, you can train your own GloVe vectors following steps.

#### 1) Remove duplicated words in the pretrained vector.
In our case, the pretrained vector is Glove.840B.300d.txt. 

Specifically for this example, remove the " " word (whitespace as a word): line 142319. 

Remove crazy (330 squares) characters: line 138701, 140649, 141505, 849063. 

#### 2) Build unigram count by running vocab_count.c
Constructs unigram counts from a corpus and the output vocab.txt will be used in step 4. 

#### 3) flatten_glove.py
Constructs a 1-dimensional array to feed into glove.C code.


#### 4) align_vocab.py
Generates new_vocab.txt for to run `/build/cooccur` (https://github.com/stanfordnlp/GloVe). This new_vocab.txt is needed to generate word-word cooccurrence statistics from a corpus. 


This step is important because Glove is being trained by looping through new_vocab.txt file, we need to align the word seqeunce in new_vocab.txt with the sequence of the pretrained GloVe vector.

#### 5) Replace Glove.C file 
with https://github.com/byorxyz/GloVe/blob/master/src/glove.c

#### 6) Run following Glove steps using your own corpus
For example,
```
./cooccur -verbose 2 -symmetric 0 -window-size 10 -vocab-file new_vocab.txt -memory 32.0 -overflow-file tempoverflow <~/Desktop/tokenizer_wrapper/tokened.txt> cooccurrences.bin

./shuffle -verbose 2 -memory 32.0 < cooccurrences.bin > cooccurrence.shuf.bin

./glove -input-file cooccurrence.shuf.bin -vocab-file new_vocab.txt -save-file glove.Wikipedia4B.300d -iter 10  -gradsq-file gradsq -verbose 2 -vector-size 300 -threads 32 -alpha 0.75 -x-max 100.0 -eta 0.05 -binary 2 -model 2
```

#### 7) sanity_check.py

Checks the sequence of the keys of the trained vectors are the same. Check the output file diff.txt to see the differences.

