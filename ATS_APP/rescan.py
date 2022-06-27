import os.path

import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ATS_Project.settings import *

stopwords = set(stopwords.words('english'))
path1 = str(BASE_DIR)
path2 = '/ATS_APP/all_skills_clean.csv'
skills = pd.read_csv(str(path1 + path2),)
print('skell set path', str(path1 + path2))
#skills = pd.read_csv(path,)


skill = skills['skills'].values

# skill

def score(seg_list01,seg_list02):
    try:
        # print('extracted skills ', skill)
        #
        # # stop_words = set(nltk.corpus.stopwords.words('english'))
        # word_tokens_01 = nltk.tokenize.word_tokenize(str(seg_list01))
        # print('str(seg_list01)')
        # print('word_tokens_01 ', word_tokens_01)
        # # remove the stop words
        # filtered_tokens_01 = [w for w in word_tokens_01 if w not in stopwords]
        #
        # # remove the punctuation
        # filtered_tokens_01 = [w for w in filtered_tokens_01 if w.isalpha()]
        #
        # # generate bigrams and trigrams (such as artificial intelligence)
        # bigrams_trigrams_01 = list(map(' '.join, nltk.everygrams(filtered_tokens_01, 2, 3)))
        #
        # # we create a set to keep the results in.
        # found_skills_01 = []
        #
        # # we search for each token in our skills database
        # for token in filtered_tokens_01:
        #     if token.lower() in skill:
        #         found_skills_01.append(token)
        #
        # # we search for each bigram and trigram in our skills database
        # for ngram in bigrams_trigrams_01:
        #     if ngram.lower() in skill:
        #         found_skills_01.append(ngram)
        #
        # print('found skills 01', found_skills_01)
        #
        # # stop_words = set(nltk.corpus.stopwords.words('english'))
        # word_tokens_02 = nltk.tokenize.word_tokenize(str(seg_list02))
        #
        # # remove the stop words
        # filtered_tokens_02 = [w for w in word_tokens_02 if w not in stopwords]
        #
        # # remove the punctuation
        # filtered_tokens_02 = [w for w in filtered_tokens_02 if w.isalpha()]
        #
        # # generate bigrams and trigrams (such as artificial intelligence)
        # bigrams_trigrams_02 = list(map(' '.join, nltk.everygrams(filtered_tokens_02, 2, 3)))
        #
        # # we create a set to keep the results in.
        # found_skills_02 = []
        #
        # # we search for each token in our skills database
        # for token in filtered_tokens_02:
        #     if token.lower() in skill:
        #         found_skills_02.add(token)
        #
        # # we search for each bigram and trigram in our skills database
        # for ngram in bigrams_trigrams_02:
        #     if ngram.lower() in skill:
        #         found_skills_02.add(ngram)
        #
        # print('found skills 02', found_skills_02)
        item01_list = re.sub('[^a-zA-Z]',' ',seg_list01)
        
        item01 =item01_list.lower().split()
        item01=[word for word in item01 if not word in stopwords]

        item02_list = re.sub('[^a-zA-Z]',' ',seg_list02)
        item02 =item02_list.lower().split()
        item02=[word2 for word2 in item02 if not word2 in stopwords]

        documents = [item01, item02]

        count_vectorizer = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
        sparse_matrix = count_vectorizer.fit_transform(documents)

        doc_term_matrix = sparse_matrix.todense()
        df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names_out(), 
                  index=['item01', 'item02'])

        answer = cosine_similarity(df, df)
        answer = pd.DataFrame(answer)
        answer = answer.iloc[[1],[0]].values[0]
        answer = round(float(answer),4)*100
    except:
        answer=0
    return answer