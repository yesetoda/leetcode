class Solution:
    def lastStoneWeight(stones: list[int]) -> int:
        srt = stones[:]
        while len(srt)>1:
            srt.sort()
            a = srt.pop()
            b = srt.pop()
            x = abs(a-b)
            if x>0:
                srt.append(x)
        return srt[0]
    print(lastStoneWeight(stones = [2,7,4,1,8,1]))