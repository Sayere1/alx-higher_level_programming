#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        best_score = 0
        top_scorer = ""
        for i in my_list:
            if a_dictionary[i] > best_score:
                best_score = a_dictionary[i]
                top_scorer = i
        return top_scorer
