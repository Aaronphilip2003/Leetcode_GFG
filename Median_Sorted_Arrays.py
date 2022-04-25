class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        sum=0
        median=0
        merged.sort()
        length=len(merged)
        if length%2!=0:
            median=merged[length//2]
        else:
            median=(merged[(length//2)-1]+merged[(length//2)])/2
        return median
        
