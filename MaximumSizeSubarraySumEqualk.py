class Solution:
    def maxSubArrayLen(nums: list[int], k: int) -> int:
        print(nums)
        mp = {0: -1}
        s = ans = 0
        for i, v in enumerate(nums):
            s += v
            if s - k in mp:
                ans = max(ans, i - mp[s - k])
            if s not in mp:
                mp[s] = i
            print(s,mp,ans)
        return ans
    print(maxSubArrayLen( nums = [1,-1,5,-2,3], k = 3))