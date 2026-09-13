class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        unique = []
        for i in range(n):
            if nums[i] not in unique:
                unique.append(nums[i])
        for i in range(len(unique)):
            nums[i]=unique[i]

        return len(unique)