#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:14:05 2018

@author: pamela
@purpose: match a given description to deescriptions of diverse books
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

def find_best_match(to_match, diverse_data, trained_tfidf):

    # convert to list
    diverse_desc = diverse_data['description'].tolist()
    
    # make into a dataframe for preprocessing
    to_match = pd.DataFrame(to_match,columns=['description'])
    # preprocess
    to_match_clean = book_descriptions(to_match)
    # tfidf
    to_match_tfidf = trained_tfidf.transform(to_match_clean)
    diverse_tfidf = trained_tfidf.transform(diverse_desc)

    # find most similar
    cosine_sim = linear_kernel(to_match_tfidf, diverse_tfidf).flatten()
    best_idx = cosine_sim.argsort()[-1]
    cosine_sim[best_idx]

    return best_idx