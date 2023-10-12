class Solution:
    def sortSentence(s: str) -> str:
        s = s.split()
        out = [0 for i in range(len(s))]
        for i in s:
            out[int(i[-1])-1] = i[:-1]
        out=" ".join(out)
        return out
    s = "is2 sentence4 This1 a3"
    print(sortSentence(s))