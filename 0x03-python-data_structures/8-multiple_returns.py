#!/usr/bin/python3
'''
Return: 0 or none
'''
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
