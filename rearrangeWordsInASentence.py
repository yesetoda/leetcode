class Solution:
    def arrangeWords( text: str) -> str:
        newword = " ".join(sorted(text.split(),key = lambda x:len(x))).lower()
        return newword[0].upper()+newword[1:]
    print(arrangeWords(text = "Keep calm and code on"))