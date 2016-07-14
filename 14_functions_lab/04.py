"""
"""

def longer_than(length, *text):
    for word in text:
        if len(word) > length:
            yield word


for i in longer_than(3, "tomer", "nir", "hello", "a"):
    print i,