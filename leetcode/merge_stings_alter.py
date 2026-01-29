# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
word1 = "ab"
word2 = "pqrs"
def mergeAlternately(word1: str, word2: str) -> str:
    result = []

    max_len = max(len(word1), len(word2))

    for i in range(max_len):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return "".join(result)

print(mergeAlternately(word1, word2))
