class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        target = len(nums)//2
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for n in dict:
            if dict.get(n)>target:
                return n
        return