class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l=m-1
        r=n-1
        idx=(m+n)-1

        while l>=0 and r>=0:
            if nums1[l]>=nums2[r]:
                nums1[idx]=nums1[l]
                idx-=1
                l-=1
            else:
                nums1[idx]=nums2[r]
                idx-=1
                r-=1

        while r>=0:
            nums1[idx]=nums2[r]
            r-=1
            idx-=1
                
        return nums1
