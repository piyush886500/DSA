class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = set()
        for i in range(len(nums1)):
            s.add(nums1[i])
        ans = set()
        for i in range(len(nums2)):
            if nums2[i] in s:
                ans.add(nums2[i])
        return list(ans)
