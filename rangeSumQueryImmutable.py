class NumArray:

    def __init__(self, nums: list[int]):
        self.nums =nums
        for i in range(1, len(self.nums)): 
            self.nums[i] = self.nums[i - 1] + self.nums[i] 
        print(self.nums)
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right]-(self.nums[left-1]if left>0 else 0)
        

a = NumArray([-2, 0, 3, -5, 2, -1])

print(a.sumRange(0,2))
print(a.sumRange(2,5))
print(a.sumRange(0,5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(self.nums)
# param_1 = obj.sumRange(left,right)