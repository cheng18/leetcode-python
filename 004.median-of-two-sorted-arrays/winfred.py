class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        result = []
        for _ in range(l // 2 + 1):
            if nums2 == [] or (nums1 and nums1[-1] > nums2[-1]):
                result.append(nums1.pop())
            else:
                result.append(nums2.pop())
                
        if l % 2 == 0:
            return (result.pop() + result.pop()) / 2
        else:
            return result.pop()
        
