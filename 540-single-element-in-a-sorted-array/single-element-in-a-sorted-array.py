class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = 1
            else:
                mp[nums[i]]+=1
        
        for x in mp:
            if mp[x]==1:
                return x
        