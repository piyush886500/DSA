class NumArray:
    total =[]
    def __init__(self, nums: List[int]):
        # self.nums=nums
        self.total = [0]*len(nums) 
        self.total[0]=nums[0]
        for i in range(1,len(nums)):
            self.total[i]=nums[i]+self.total[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.total[right]
        return self.total[right]-self.total[left-1]
        


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)