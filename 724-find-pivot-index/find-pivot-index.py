class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n= len(nums)
        total=[0]*n
        total[0]=nums[0]
        for i in range(1,n):
            total[i]=nums[i]+total[i-1]
        for i in range(n):
            if i==0:
                left=0
            else:
                left = total[i-1]
            right = total[n-1]-total[i]
            if left==right:
                return i
        return -1