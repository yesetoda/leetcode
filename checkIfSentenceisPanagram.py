class Solution:

    def checkIfPangram( sentence: str) -> bool:
        letters = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        sentences =set(i for i in sentence)
        return sentences & letters == letters
    sentence = "thquickbrownfoxjumpsoverthelazydog"
    print(checkIfPangram(sentence))