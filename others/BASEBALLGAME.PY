class Solution:
    def calPoints(operations: list[str]) -> int:
        score = []
        for i in operations:
            # print(score)
            if i.isnumeric():
                score.append(int(i))
            elif i[0] == '-':
                score.append(0-int(i[1:]))
            elif i == "+":
                num1 = score[-1]
                num2 = score[-2]
                score.append(num1+num2)
            elif i == "D":
                num1 = score[-1]
                score.append(num1*2)
            elif i == "C":
                num1 = score.pop()
        totScore = sum(score)
        return totScore
    ops = ["1","C"]
    print(calPoints(ops))
        