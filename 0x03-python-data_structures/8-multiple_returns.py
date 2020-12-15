#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is 0:
        return 0, ""
    length = len(sentence)
    first = sentence[0]
    return (length, first)

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))