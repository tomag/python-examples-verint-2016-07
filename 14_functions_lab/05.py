"""
"""
from collections import defaultdict

def groupby(func, *words):
    grouped = defaultdict(list)
    for word in words: 
        key = func(word)
        grouped[key].append(word)
    return grouped


result = groupby(lambda(s): s[0], "hello", "hi", "help", "bye", "here")
print result