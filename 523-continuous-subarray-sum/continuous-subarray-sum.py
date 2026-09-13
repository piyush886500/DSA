class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0:-1}
        n=len(nums)
        prefixsum=0
        rem=0
        for i in range(n):
            prefixsum+=nums[i]
            rem = prefixsum%k
            if rem in map :
                if i-map[rem]>=2:
                    return True
            else:
                map[rem]=i
            
        return False
