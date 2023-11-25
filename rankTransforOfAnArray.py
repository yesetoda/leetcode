class Solution:
    def arrayRankTransform(arr: list[int]) -> list[int]:
        a = sorted(list(set(arr)))
        d = {a[i]:i+1 for i in range(len(a))}
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr
    arrayRankTransform(arr = [40,10,20,30])