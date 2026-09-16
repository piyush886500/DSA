class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l=0
        r=len(nums)-1
        count=0
        if len(nums)==1 :
            if nums[0]==val:
                return 0
            else:
                return 1
        while l<=r:
            if nums[l]==val:
                if nums[l]==nums[r]:
                    r-=1
                else:
                    count+=1
                    temp=nums[l]
                    nums[l]=nums[r]
                    nums[r]=temp
                    l+=1
            else:
                count+=1
                l+=1
        return count

