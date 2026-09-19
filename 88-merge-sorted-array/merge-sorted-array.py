class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        k=0
        for i in range(m,m+n):
            if k<n:
                nums1[i]=nums2[k]
                k+=1

        nums1.sort()
        return nums1
        