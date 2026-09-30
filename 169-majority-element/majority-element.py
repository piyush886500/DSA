class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        target = len(nums)//2
        freq=1
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                freq+=1
            else:
                freq=1
                ans=nums[i]
            if freq>target:
                return nums[i]
        return ans