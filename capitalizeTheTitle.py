class Solution:
    def capitalizeTitle( title: str) -> str:
        out =""
        for i in title.split():
            if len(i)<=2:
                out+=i.lower()+" "
            else:
                out+=i[0].upper()+i[1:].lower()+" "
        return out
    title = "i lOve leetcode"
    print(capitalizeTitle(title))