class Solution:
    def minMeetingRooms( intervals: list[list[int]]) -> int:
        ps = [0]*(40+1)
        for i in intervals:
            ps[i[0]] += 1
            ps[i[1]] -= 1
        print("this is ps",ps)
        from itertools import accumulate
        ls = ps
        prefixsum = list(accumulate(ls))
        print(prefixsum)
        print(max(prefixsum))
    print(minMeetingRooms(intervals = [[0,30],[5,10],[15,20]]))