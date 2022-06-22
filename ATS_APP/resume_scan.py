import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from . import utils
  
stopwords = set(stopwords.words('english'))

def score(seg_list01,seg_list02):
    try:

        item01_list = re.sub('[^a-zA-Z]',' ',seg_list01)
        item01 =item01_list.lower().split()

        #item01 = utils.clean_text(item01)
        #item01 = utils.remove_punctuation(item01)


        item01=[word for word in item01 if not word in stopwords]
        print('item01 ', item01)

        item02_list = re.sub('[^a-zA-Z]',' ',seg_list02)
        item02 =item02_list.lower().split()

        #item02 = utils.clean_text(item02)
        #item02 = utils.remove_punctuation(item02)

        item02=[word2 for word2 in item02 if not word2 in stopwords]
        print('item02 ', item02)
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
