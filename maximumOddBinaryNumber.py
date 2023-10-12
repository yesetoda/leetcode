class Solution:
    def maximumOddBinaryNumber(s: str) -> str:
        ones = s.count("1")
        out = ["0" for i in range(len(s))]
        # print(out)
        for i in range(ones-1):
            out[i] = "1"
        return "".join(out[:len(s)-1])+"1"
        ones = s.count("1")
        out = ""
        for i in range(len(s)-1):
            if i<ones-1:
                out+= "1"
            else:
                out+="0"
            # print(out)
        return out+"1"
    print(maximumOddBinaryNumber("001"))