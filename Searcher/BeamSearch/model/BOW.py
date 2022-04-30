import pandas as pd
import numpy as np


def calculateBOW(wordset,l_doc):
    tf_diz = dict.fromkeys(wordset,0)
    for word in l_doc:
        tf_diz[word]=l_doc.count(word)
    return tf_diz

def get_scores(bow_q:list, bow_v:list):
    bow_q_size = len(bow_q)
    bow_v_size = len(bow_v)

    wordset = np.union1d(bow_q, bow_v)
    bow1 = calculateBOW(wordset, bow_q)
    bow2 = calculateBOW(wordset, bow_v)
    df_bow = pd.DataFrame([bow1, bow2])

    intersection_idx = [i for i, v in enumerate(df_bow.values[0]) if v == df_bow.values[1][i]]
    intersection = len(intersection_idx)
    score_relevant = intersection / bow_q_size
    score_irrelevant = intersection / bow_v_size
    if (score_relevant + score_irrelevant) == 0: return 0
    return (2 * score_relevant * score_irrelevant) / (score_relevant + score_irrelevant)



if __name__ == '__main__':
    doc1 = 'a'
    doc2 = 'a b c e f'
    doc1 = doc1.lower().split()
    doc2 = doc2.lower().split()
    score = get_scores(doc1 , doc2)
    print(score)
