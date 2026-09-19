class Solution:
    def reverse(self,nums,l,r):
        while l < r:
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            l+=1
            r-=1
        return nums
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k%=n
         
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        return nums