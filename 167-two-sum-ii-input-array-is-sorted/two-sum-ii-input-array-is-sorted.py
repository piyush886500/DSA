class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map ={}
        l=0
        r=len(numbers)-1
        ans =[0]*2
        while l<r:
            total=numbers[l]+numbers[r]
            if total==target:
                ans[0]=l+1
                ans[1]=r+1
                return ans
            if total>target:
                r-=1
            else:
                l+=1

        # for l in range(len(numbers)):
        #     total = target-numbers[l]
        #     if total in map:
        #         ans[0]=map[total]+1
        #         ans[1]=l+1
        #         return ans
        #     else:
        #         map[numbers[l]]=l
        return ans

