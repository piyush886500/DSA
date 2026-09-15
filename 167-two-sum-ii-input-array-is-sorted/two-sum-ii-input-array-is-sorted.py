class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map ={}
        l=0
        r=len(numbers)-1
        ans =[0]*2
        for l in range(len(numbers)):
            total = target-numbers[l]
            if total in map:
                ans[0]=map[total]+1
                ans[1]=l+1
                return ans
            else:
                map[numbers[l]]=l
        return ans

