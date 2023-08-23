class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def add(self, val):
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse = True)
        print(self.nums[self.k-1], self.nums)

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(4, [8, 5, 4, 3, 2])
# param_1 = obj.add(3)
# param_1 = obj.add(5)
# param_1 = obj.add(10)
# param_1 = obj.add(9)
# param_1 = obj.add(4)