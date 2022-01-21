import pandas as pd
import numpy as np
import collections


def calculateBOW(wordset,l_doc):
  tf_diz = dict.fromkeys(wordset,0)
  for word in l_doc:
      tf_diz[word]=l_doc.count(word)
  return tf_diz



def main():
    doc1 = 'Game of Thrones is an amazing tv series!'
    doc2 = 'Game of Thrones is the best tv tv series!'
    doc1 = doc1.lower().split()
    doc2 = doc2.lower().split()
    wordset = np.union1d(doc1,doc2)
    bow1 = calculateBOW(wordset, doc1)
    bow2 = calculateBOW(wordset, doc2)
    df_bow = pd.DataFrame([bow1, bow2])
    print(df_bow)



if __name__ == '__main__':
    main()